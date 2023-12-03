const path = require("path");

module.exports = {
  // Other webpack configurations...

  module: {
    rules: [
      // Other rules...

      {
        test: /\.(png|jpg|gif)$/i,
        use: [
          {
            loader: "file-loader",
          },
        ],
      },
    ],
  },
};
