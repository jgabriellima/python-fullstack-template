/* eslint-disable */
const path = require('path');
module.exports = {
    publicPath: process.env.BASE_URL,
    outputDir: path.resolve(__dirname, '../app/templates'),
    // runtimeCompiler: undefined,
    // productionSourceMap: undefined,
    // parallel: undefined,
    // css: undefined,
    chainWebpack: (config) => {
        if (process.env.NODE_ENV === 'production') {
            config.module.rule('vue').uses.delete('cache-loader');
            config.module.rule('js').uses.delete('cache-loader');
            config.module.rule('ts').uses.delete('cache-loader');
            config.module.rule('tsx').uses.delete('cache-loader');
        }
    },
};