SELECT c.nome, v.modelo, o.descricao, o.valor
FROM ordens_servico o
INNER JOIN veiculos v ON o.id_veiculo = v.id_veiculo
INNER JOIN clientes c ON v.id_cliente = c.id_cliente;

SELECT c.nome, v.modelo
FROM clientes c
LEFT JOIN veiculos v ON c.id_cliente = v.id_cliente;
