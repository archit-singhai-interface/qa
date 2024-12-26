# QA Bot

### Local Setup
The frontend is build using React and is present in the `client` directory. Run it using the below command.
```bash
cd client
npm install
npm run dev
```

The backend is built using FastAPI and is present in the `server/bot` directory. Run it using the below command.
**Note:** Make sure to add env variables in a `.env` file in the `server/bot` directory.
```bash
cd server
poetry install
uvicorn main:app --reload
```

**Note:** When new files are added or changed, make sure to remove the `storage` folder in the `server/bot` directory. This is to create a new `storage` folder with the new files.

### TODO:
1. Make the frontend responsive