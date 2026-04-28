CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE veiculos (
    id_veiculo SERIAL PRIMARY KEY,
    modelo VARCHAR(100),
    placa VARCHAR(10),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE ordens_servico (
    id_os SERIAL PRIMARY KEY,
    descricao TEXT,
    valor DECIMAL(10,2),
    id_veiculo INT,
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)
);
