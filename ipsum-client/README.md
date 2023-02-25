# ipsum-client

[![Check Client](https://github.com/dtrifuno/ipsum/actions/workflows/check-client.yml/badge.svg)](https://github.com/dtrifuno/ipsum/actions/workflows/check-client.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a [Next.js](https://nextjs.org/) frontend to the
[`ipsum`](https://github.com/dtrifuno/ipsum/tree/main/ipsum) placeholder text
library. It requires the
[`ipsum-server`](https://github.com/dtrifuno/ipsum/tree/main/ipsum-server) backend.

You can access a deployed version of Ipsum from your browser by going to
[ipsum.trifunovski.me](https://ipsum.trifunovski.me).

![Screenshot of Ipsum in action.](https://raw.githubusercontent.com/dtrifuno/ipsum/main/ipsum-client/public/screenshot.png)

## Usage

### Development

First, run the development server:

```bash
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

Use `yarn typecheck` or `yarn lint` to typecheck and lint the project respectively.

### Deployment

Run

```bash
yarn export
```

and copy the `out/` folder to the deployment server.

## License

[MIT](https://raw.githubusercontent.com/dtrifuno/ipsum/main/ipsum-client/LICENSE.md)
