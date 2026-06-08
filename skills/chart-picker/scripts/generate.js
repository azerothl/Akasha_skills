#!/usr/bin/env node
/** Minimal chart config emitter — extend with AntV as needed. */
const fs = require("fs");
const type = process.argv[2] || "bar";
const dataPath = process.argv[3];
let data = [];
if (dataPath && fs.existsSync(dataPath)) {
  data = JSON.parse(fs.readFileSync(dataPath, "utf8"));
}
console.log(JSON.stringify({ type, dataSample: data.slice(0, 5), hint: "Import @antv/g2plot in your app" }, null, 2));
