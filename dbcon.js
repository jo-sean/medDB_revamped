var mysql = require('mysql');
var pool = mysql.createPool({
  connectionLimit: 10,
  host: 'classmysql.engr.oregonstate.edu',
  user: 'cs340_perezjos',
  password: 'Hkdi6ton!',
  database: 'cs340_perezjos'
});
module.exports.pool = pool;
