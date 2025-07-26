# Hello Ubucon! Welcome to 12-factor ExpressJS app!

<p align="center">
    <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--MgAyrZbI--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1024/1%2AhYfdBkfKgvtMoDcqk_LjWA.png">
</p>

This is a simple example of a 12-factor ExpressJS application. It's built using the ExpressJS framework.
This application is built using the [express-generator](https://expressjs.com/en/starter/generator.html)
and exposes 3 endpoints:
- /health
- /fibonacci/:number (requires postgresql database)
- /keys

## Prerequisites

- [NodeJS && NPM](https://nodejs.org/en/download)


## How to run it locally?

0. Change the working directory: `cd expressjs-hello-world/app`
1. Install dependencies: `npm install`
2. Run the server: `npm start`
4. Test the endpoints using the following curl commands
  - `curl http://localhost:3000/health`
  - `curl http://localhost:3000/fibonacci/9`
5. Congratulations! You've finished exploring the ExpressJS Hello World project!

## Next steps

Let's start packaging! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/expressjs-01-rock) `git checkout expressjs-01-rock`
