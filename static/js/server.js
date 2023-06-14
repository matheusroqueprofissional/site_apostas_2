const express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000;

// Configurações de conexão com o banco de dados
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'si'
});

// Conectar ao banco de dados
connection.connect(function(err) {
  if (err) {
    console.error('Erro ao conectar ao banco de dados:', err);
    return;
  }
  console.log('Conexão com o banco de dados estabelecida com sucesso.');
});

// Rota para receber a requisição POST e inserir os dados no banco de dados
app.post('/api/palpites', (req, res) => {
  const { username, palpite } = req.body;

  // Montar a consulta SQL
  const query = `INSERT INTO palpite (username, palpite) VALUES (?, ?)`;
  const values = [username, palpite];

  // Executar a consulta SQL
  connection.query(query, values, function(error, results) {
    if (error) {
      console.error('Erro ao executar a consulta:', error);
      res.status(500).send('Erro ao inserir os dados no banco de dados.');
    } else {
      console.log('Dados inseridos com sucesso na tabela palpite.');
      res.status(200).send('Dados inseridos com sucesso.');
    }
  });
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}.`);
});
