import os
import json
from pathlib import Path
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import tiktoken

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentAnalyzerLLM:
    def __init__(self, docs_path: str):
        self.docs_path = docs_path
        self.summaries = {}
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
        
        # Build document hierarchy
        self.hierarchy = self._build_hierarchy()
        logger.info("Document hierarchy built")

    def _build_hierarchy(self) -> dict:
        """Build a hierarchical structure of the documentation."""
        hierarchy = {}
        
        for root, dirs, files in os.walk(self.docs_path):
            if '.git' in dirs:  # Skip git directories
                dirs.remove('.git')
                
            rel_path = os.path.relpath(root, self.docs_path)
            if rel_path == '.':
                continue
                
            path_parts = rel_path.split(os.sep)
            current = hierarchy
            
            # Build the path in the hierarchy
            for part in path_parts:
                if part not in current:
                    current[part] = {'_files': []}
                current = current[part]
            
            # Add files at this level
            current['_files'].extend([f for f in files if f.endswith('.md')])
        
        return hierarchy

    def _get_document_context(self, file_path: str) -> str:
        """Get the hierarchical context of a document."""
        rel_path = os.path.relpath(file_path, self.docs_path)
        path_parts = rel_path.split(os.sep)
        
        if len(path_parts) <= 1:
            return "Root level document"
        
        section = path_parts[0]
        return f"Document in section: {section}"

    def count_tokens(self, text: str) -> int:
        """Count tokens in text."""
        return len(self.tokenizer.encode(text))

    def chunk_content(self, content: str, max_tokens: int = 6000) -> list[str]:
        """Split content into chunks that fit within token limit."""
        chunks = []
        current_chunk = []
        current_length = 0
        
        for line in content.split('\n'):
            line_tokens = self.count_tokens(line)
            
            if current_length + line_tokens > max_tokens:
                chunks.append('\n'.join(current_chunk))
                current_chunk = [line]
                current_length = line_tokens
            else:
                current_chunk.append(line)
                current_length += line_tokens
        
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks

    def analyze_document(self, file_path: str) -> dict:
        """Analyze a single markdown document using LLM."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Get document context
            doc_context = self._get_document_context(file_path)
            
            # Split content into manageable chunks if needed
            chunks = self.chunk_content(content)
            chunk_summaries = []

            for i, chunk in enumerate(chunks):
                messages = [
                    SystemMessage(content=f"""You are a technical documentation analyzer. 
                    This document is {doc_context}.
                    Analyze the provided markdown content and create a detailed summary including:
                    1. Main topics and themes
                    2. Key concepts explained
                    3. Important code examples or technical details
                    4. Document structure and organization
                    5. How this content relates to its section
                    Be concise but comprehensive."""),
                    HumanMessage(content=f"Analyze this markdown content{' (chunk '+str(i+1)+')' if len(chunks)>1 else ''}:\n\n{chunk}")
                ]

                response = self.llm.invoke(messages)
                chunk_summaries.append(response.content)

            # If we had multiple chunks, get an overall summary
            if len(chunks) > 1:
                messages = [
                    SystemMessage(content=f"""Combine these chunk summaries into one coherent document analysis.
                    Remember this is {doc_context}.
                    Focus on the overall structure and main themes."""),
                    HumanMessage(content=f"Chunk summaries:\n\n" + "\n\n".join(chunk_summaries))
                ]
                final_summary = self.llm.invoke(messages).content
            else:
                final_summary = chunk_summaries[0]

            # Get key topics with section context
            messages = [
                SystemMessage(content=f"""Extract 5-10 key topics from this document as a JSON array.
                Consider that this is {doc_context}.
                Each topic should be a string of 1-3 words."""),
                HumanMessage(content=final_summary)
            ]
            topics_response = self.llm.invoke(messages)
            try:
                topics = json.loads(topics_response.content)
            except:
                topics = []
                logger.warning(f"Could not parse topics for {file_path}")

            return {
                'file_name': Path(file_path).name,
                'path': file_path,
                'section': self._get_document_context(file_path),
                'size_bytes': len(content),
                'summary': final_summary,
                'key_topics': topics,
                'num_chunks': len(chunks)
            }

        except Exception as e:
            logger.error(f"Error analyzing {file_path}: {str(e)}")
            return None

    def analyze_all_documents(self):
        """Analyze all markdown files in the directory."""
        try:
            # Find all MD files
            md_files = []
            for root, _, files in os.walk(self.docs_path):
                for file in files:
                    if file.endswith('.md'):
                        md_files.append(os.path.join(root, file))
            
            logger.info(f"Found {len(md_files)} markdown files")
            
            # Analyze each file
            for file_path in md_files:
                logger.info(f"Analyzing {file_path}")
                analysis = self.analyze_document(file_path)
                if analysis:
                    self.summaries[file_path] = analysis
            
            # Save results
            output_path = os.path.join(self.docs_path, "document_analysis_llm.json")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.summaries, f, indent=2)
            
            # Generate readable report
            report_path = os.path.join(self.docs_path, "document_analysis_llm.md")
            self.generate_report(report_path)
            
            logger.info(f"Analysis complete. Results saved to {output_path} and {report_path}")
            
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            raise

    def generate_report(self, output_path: str):
        """Generate analysis reports."""
        try:
            # Generate structured documentation
            doc_structure = self.generate_document_structure()
            
            # Save structure
            structure_path = os.path.join(os.path.dirname(output_path), "document_structure.json")
            with open(structure_path, 'w', encoding='utf-8') as f:
                json.dump(doc_structure, f, indent=2)
            
            # Continue with regular report generation...
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise

    def _write_hierarchy(self, f, hierarchy, level=0):
        """Write the document hierarchy in tree format."""
        indent = "  " * level
        for key, value in hierarchy.items():
            if key == '_files':
                for file in value:
                    f.write(f"{indent}├── {file}\n")
            else:
                f.write(f"{indent}├── {key}/\n")
                self._write_hierarchy(f, value, level + 1)

    def generate_document_structure(self) -> dict:
        """Generate a structured documentation tree similar to structure.json."""
        try:
            documentation_tree = {
                "documentation_tree": {
                    "root_path": os.path.basename(self.docs_path),
                    "sections": [],
                    "metadata": {
                        "relationships": {
                            "fulfillment_hierarchy": {
                                "primary": "FBA",
                                "alternatives": ["Seller Fulfilled Prime", "Multi-Location Inventory"],
                                "supporting": ["Custom returns", "Delivery Services"]
                            },
                            "document_types": {
                                "foundation": ["policies", "requirements", "getting started"],
                                "operational": ["returns", "delivery", "inventory"],
                                "reference": ["FAQ", "best practices", "guides"]
                            }
                        }
                    }
                }
            }

            # Group documents by section
            sections = {}
            for file_path, analysis in self.summaries.items():
                section_name = os.path.basename(os.path.dirname(file_path))
                if section_name not in sections:
                    sections[section_name] = {
                        "title": section_name,
                        "path": os.path.join(self.docs_path, section_name),
                        "documents": []
                    }

                # Extract headings from the content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    headings = self._extract_headings(content)

                # Create document entry
                doc_entry = {
                    "title": analysis["file_name"].replace(".md", ""),
                    "filename": analysis["file_name"],
                    "url": f"https://sellercentral.amazon.com/help/hub/reference/{self._generate_reference_id(file_path)}",
                    "context": {
                        "section_type": self._determine_section_type(section_name),
                        "position": self._determine_position(analysis),
                        "prerequisites": self._find_prerequisites(analysis),
                        "followed_by": self._find_followed_by(analysis),
                        "related_topics": analysis.get("key_topics", []),
                        "headings": headings,
                        "cross_references": self._find_cross_references(content)
                    }
                }
                sections[section_name]["documents"].append(doc_entry)

            documentation_tree["documentation_tree"]["sections"] = list(sections.values())
            return documentation_tree

        except Exception as e:
            logger.error(f"Error generating document structure: {str(e)}")
            raise

    def _extract_headings(self, content: str) -> list:
        """Extract all markdown headings from content."""
        headings = []
        for line in content.split('\n'):
            if line.strip().startswith('#'):
                level = len(line.split()[0])  # Count the number of #
                text = line.strip('#').strip()
                headings.append({
                    "level": level,
                    "text": text
                })
        return headings

    def _determine_section_type(self, section_name: str) -> str:
        """Determine the type of section based on its name."""
        section_types = {
            "Get started with Fulfillment by Amazon FBA": "core_fba",
            "Seller Flex and Alternative Fulfillment": "alternative_fulfillment",
            "Service and Delivery Management": "service_management"
        }
        return section_types.get(section_name, "general")

    def _determine_position(self, analysis: dict) -> str:
        """Determine the document's position in the hierarchy."""
        summary = analysis.get("summary", "").lower()
        if any(word in summary for word in ["policy", "requirement", "introduction", "getting started"]):
            return "foundation"
        elif any(word in summary for word in ["operation", "manage", "process"]):
            return "operational"
        return "reference"

    def _find_prerequisites(self, analysis: dict) -> list:
        """Find prerequisite documents based on analysis."""
        prerequisites = []
        summary = analysis.get("summary", "").lower()
        if "prerequisite" in summary or "requires" in summary:
            # Extract mentioned documents
            # This is a simplified version - you might want to make it more sophisticated
            for topic in analysis.get("key_topics", []):
                if "prerequisite" in topic.lower():
                    prerequisites.append(topic)
        return prerequisites

    def _find_followed_by(self, analysis: dict) -> list:
        """Find documents that should follow this one."""
        followed_by = []
        summary = analysis.get("summary", "").lower()
        if "next step" in summary or "following" in summary:
            # Extract mentioned next steps
            for topic in analysis.get("key_topics", []):
                if "next" in topic.lower():
                    followed_by.append(topic)
        return followed_by

    def _find_cross_references(self, content: str) -> dict:
        """Find cross-references in the content."""
        cross_refs = {
            "internal": {"links": []},
            "external": {"links": []}
        }
        
        # Find markdown links
        import re
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        
        for title, url in links:
            if "amazon.com" in url or url.startswith("/"):
                cross_refs["internal"]["links"].append({
                    "title": title,
                    "path": url
                })
            else:
                cross_refs["external"]["links"].append({
                    "title": title,
                    "url": url
                })
        
        return cross_refs

    def _generate_reference_id(self, file_path: str) -> str:
        """Generate a reference ID for the document URL."""
        # This is a placeholder - you would need to implement your own logic
        # to generate or lookup actual reference IDs
        import hashlib
        return "G" + hashlib.md5(file_path.encode()).hexdigest()[:9].upper()

if __name__ == "__main__":
    # Usage
    docs_path = "/home/dumball/Downloads/interface-qa-bot-main/amazon_help_pages_us"  # Replace with your docs path
    analyzer = DocumentAnalyzerLLM(docs_path)
    analyzer.analyze_all_documents() 