

CREATE TABLE realizar_orcamento (
Codigo int not null auto_increment,
Nome_Produto varchar(100) not null,
Descrição_Produto longtext,
Unidade int(50) NOT NULL ,
Qtd int(255) NOT NULL,
Desconto DOUBLE NOT NULL,
Preco_uni DOUBLE NOT NULL,
Preco_total DOUBLE NOT NULL,
Frete DOUBLE NOT NULL,
primary key(codigo)
); 


