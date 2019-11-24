'use strict';
const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: [
        './src/js/index.js',
        './src/css/style.css',
    ],
    output: {
        path: path.resolve(__dirname, './static'),
        filename: 'js/bundle.js'
    },
    devtool: "source-map",
    module: {
        rules: [
            {
                test: /\.js$/,
                include: path.resolve(__dirname, 'src/js'),
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }},
            {
                test: /\.css$/,
                include: path.resolve(__dirname, 'src/css'),
                use: [
                    {
                      loader: MiniCssExtractPlugin.loader,
                    },
                    {
                        loader: "css-loader",
                        options: {
                            sourceMap: true,
                            url: false
                        }
                    }
                ]
            }
            ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: './css/style.bundle.css',
            allChunks: true
        }),
        new CleanWebpackPlugin(),
        new CopyWebpackPlugin([
            {
                from: './src/fonts',
                to: './fonts'
            },
            {
                from: './src/img',
                to: './img'
            }
        ])
    ]
};

