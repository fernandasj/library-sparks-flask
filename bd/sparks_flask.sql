create table livro(
id_livro serial not null,
titulo varchar(100) not null,
autor varchar(100) not null,
editora varchar(50) not null,
local_edicao varchar(100) not null,
data_edicao date not null,
status varchar(50) not null,
primary key(id_livro)
);

create table usuario(
id_usuario serial not null,
username varchar (100) not null,
senha varchar(100) not null,
primary key (id_usuario)
);

create table reserva(
id_reserva serial not null,
id_usuario integer not null,
id_livro integer not null,
primary key(id_reserva),
foreign key(id_usuario) references usuario (id_usuario),
foreign key(id_livro) references livro (id_livro)
);

create table emprestimo(
id_emprestimo serial not null,
id_usuario integer not null,
id_livro integer not null,
data_emprestimo date not null,
primary key(id_emprestimo),
foreign key(id_usuario) references usuario(id_usuario),
foreign key(id_livro) references livro(id_livro)
);

insert into usuario (username, senha) values ('fernanda', '1q2w3e4r5t');
insert into livro (titulo, autor, editora, local_edicao, data_edicao, status) values ('Inferno', 'Dan Brown','Arqueiro', 'Sao Paulo', '2012-08-13', 'disponivel');
insert into livro (titulo, autor, editora, local_edicao, data_edicao, status) values ('Um dia', 'David Nichols', 'Intrinseca', 'Rio de Janeiro', '2011-03-10', 'emprestado');
insert into livro (titulo, autor, editora, local_edicao, data_edicao, status) values ('Fallen', 'Lauren Kate', 'Galera', 'Sao Paulo', '2003-05-03', 'reservado');
insert into livro (titulo, autor, editora, local_edicao, data_edicao, status) values ('A escolha', 'Nocholas Sparks', 'Novo Conceito', 'Rio de Janeiro', '2015-10-04', 'disponivel');
insert into livro (titulo, autor, editora, local_edicao, data_edicao, status) values ('Teardrop', 'Lauren Kate', 'Galera', 'Sao Paulo', '2014-05-06', 'emprestado');

