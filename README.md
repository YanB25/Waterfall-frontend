# Waterfall-frontend
Waterfall-frontend is the frontend of the project [waterfall](https://github.com/wwyf/Waterfall).

It bases on [Vuejs](https://vuejs.org/) and [elementUI](https://madewithvuejs.com/element-ui).
## Install
### Prerequisite
- yarn: 1.12.3
- node: v11.1.0
- npm: 6.4.1


### Install 
Clone or download this repository, and

``` bash
cd Waterfall-frontend
yarn
```

## Deploy
### ... in development mode

``` bash
npm run dev
```
## ... in production mode

``` bash
npm run build
```
It generates bundled files(e.g. `index.html` and `index.js`) to `dict/`. A http server(like `nginx`) is needed to serve them.

## docker
To build the project into docker image, it's as simple as

``` bash
docker build .
```