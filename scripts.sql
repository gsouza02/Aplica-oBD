CREATE DATABASE IF NOT EXISTS catalogo_jogos;

USE catalogo_jogos;

-- Tabela de Desenvolvedores
CREATE TABLE IF NOT EXISTS desenvolvedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    pais VARCHAR(50) NOT NULL
);

-- Tabela de Gêneros
CREATE TABLE IF NOT EXISTS genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Tabela de Plataformas
CREATE TABLE IF NOT EXISTS plataforma (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    fabricante VARCHAR(50)
);

-- Tabela de Jogos
CREATE TABLE IF NOT EXISTS jogo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    ano_lancamento YEAR NOT NULL,
    id_desenvolvedor INT,
    id_genero INT,
    FOREIGN KEY (id_desenvolvedor) REFERENCES desenvolvedor(id),
    FOREIGN KEY (id_genero) REFERENCES genero(id)
);

-- Tabela relacional para associar jogos às plataformas
CREATE TABLE IF NOT EXISTS jogo_plataforma (
    id_jogo INT,
    id_plataforma INT,
    PRIMARY KEY (id_jogo, id_plataforma),
    FOREIGN KEY (id_jogo) REFERENCES jogo(id),
    FOREIGN KEY (id_plataforma) REFERENCES plataforma(id)
);

-- Tabela de Lista de Desejos
CREATE TABLE IF NOT EXISTS lista_desejos (
    id_jogo INT,
    data_adicao DATE,
    PRIMARY KEY (id_jogo),
    FOREIGN KEY (id_jogo) REFERENCES jogo(id)
);

-- Inserir desenvolvedores
INSERT INTO desenvolvedor (nome, pais) VALUES
('Nintendo', 'Japão'),
('CD Projekt Red', 'Polônia'),
('Ubisoft', 'França'),
('Bethesda', 'EUA'),
('Rockstar Games', 'EUA'),
('Naughty Dog', 'EUA'),
('Square Enix', 'Japão'),
('Sony', 'Japão'),
('Electronic Arts', 'EUA'),
('Valve', 'EUA');

-- Inserir gêneros
INSERT INTO genero (nome) VALUES
('Ação'), 
('RPG'), 
('Estratégia'), 
('Simulação'), 
('Aventura'), 
('Terror');

-- Inserir plataformas
INSERT INTO plataforma (nome, fabricante) VALUES
('PC', 'Microsoft'),
('PlayStation 5', 'Sony'),
('Nintendo Switch', 'Nintendo'),
('Xbox Series X', 'Microsoft'),
('PlayStation 4', 'Sony'),
('PC VR', 'Vários'),
('Nintendo 3DS', 'Nintendo');

-- Inserir jogos
INSERT INTO jogo (titulo, ano_lancamento, id_desenvolvedor, id_genero) VALUES
('The Legend of Zelda: Breath of the Wild', 2017, 1, 5),
('Cyberpunk 2077', 2020, 2, 2),
('Assassin\'s Creed Valhalla', 2020, 3, 1),
('The Witcher 3: Wild Hunt', 2015, 2, 2),
('Red Dead Redemption 2', 2018, 5, 1),
('The Last of Us Part II', 2020, 6, 5),
('Final Fantasy XV', 2016, 7, 2),
('Spider-Man: Miles Morales', 2020, 8, 1),
('Battlefield V', 2018, 9, 1),
('Half-Life: Alyx', 2020, 10, 4),
('God of War', 2018, 6, 1),
('Horizon Zero Dawn', 2017, 6, 1),
('Grand Theft Auto V', 2013, 5, 1),
('Minecraft', 2011, 10, 1),
('Overwatch', 2016, 9, 1),
('Bloodborne', 2015, 6, 5),
('Sekiro: Shadows Die Twice', 2019, 6, 1),
('Persona 5', 2016, 7, 2),
('Resident Evil 7', 2017, 4, 6),
('The Elder Scrolls V: Skyrim', 2011, 4, 2),
('Doom Eternal', 2020, 4, 1),
('Mario Kart 8 Deluxe', 2017, 1, 1),
('The Sims 4', 2014, 9, 4),
('FIFA 21', 2020, 9, 1),
('Street Fighter V', 2016, 9, 1),
('Star Wars Jedi: Fallen Order', 2019, 9, 2),
('Mortal Kombat 11', 2019, 9, 1),
('Dark Souls III', 2016, 6, 1),
('Dying Light', 2015, 3, 6);
