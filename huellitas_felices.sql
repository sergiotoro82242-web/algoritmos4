create database veterinaria_huellitas;
use veterinaria_huellitas;

--  PROPIETARIO
create table propietario (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    tipo_documento enum('cc','ti','pasaporte','otro') not null,
    numero_documento varchar(50) not null unique,
    telefono varchar(20),
    email varchar(100) unique,
    created_at timestamp default current_timestamp
);

-- MASCOTA
create table mascota (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    especie enum('perro','gato','ave','reptil','otro') not null,
    especie_otro varchar(50),
    raza varchar(50),
    edad int,
    peso decimal(5,2),
    propietario_id int not null,
    foreign key (propietario_id) references propietario(id)
        on delete cascade
);

--  CITA
create table cita (
    id int auto_increment primary key,
    fecha date not null,
    hora time not null,
    tipo enum('consulta','esterilizacion','control','vacunacion','urgencia') not null,
    motivo text,
    duracion int,
    estado enum('agendada','cancelada','reprogramada','no_asistio','finalizada') default 'agendada',
    mascota_id int not null,
    foreign key (mascota_id) references mascota(id)
        on delete cascade
);

--  ATENCION
create table atencion (
    id int auto_increment primary key,
    cita_id int,
    mascota_id int not null,
    fecha date not null,
    diagnostico text,
    procedimiento text,
    observaciones text,
    foreign key (mascota_id) references mascota(id)
        on delete cascade,
    foreign key (cita_id) references cita(id)
        on delete set null
);

-- 💊 TRATAMIENTO
create table tratamiento (
    id int auto_increment primary key,
    mascota_id int not null,
    descripcion text not null,
    fecha_inicio date,
    fecha_fin date,
    estado enum('activo','finalizado') default 'activo',
    foreign key (mascota_id) references mascota(id)
        on delete cascade
);

--  APLICACION
create table aplicacion (
    id int auto_increment primary key,
    mascota_id int not null,
    tipo enum('vacuna','medicamento') not null,
    nombre varchar(100) not null,
    fecha date not null,
    proxima_fecha date,
    foreign key (mascota_id) references mascota(id)
        on delete cascade
);

--  RECORDATORIO
create table recordatorio (
    id int auto_increment primary key,
    mascota_id int not null,
    mensaje varchar(200) not null,
    fecha date not null,
    tipo enum('cita','vacuna','tratamiento') not null,
    enviado boolean default false,
    foreign key (mascota_id) references mascota(id)
        on delete cascade
);

--  USUARIO
create table usuario (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    username varchar(50) unique not null,
    contraseña varchar(255) not null
);
 -- VETERINARIO
create table veterinario (
    id int auto_increment primary key,
    usuario_id int,
    especialidad varchar(100),
    foreign key (usuario_id) references usuario(id)
);

alter table cita add veterinario_id int;
alter table cita add foreign key (veterinario_id) references veterinario(id);

alter table atencion add veterinario_id int;
alter table atencion add foreign key (veterinario_id) references veterinario(id);

-- MEDICAMENTO
create table medicamento (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    descripcion text
);
alter table aplicacion
add medicamento_id int;
alter table aplicacion
add constraint fk_aplicacion_medicamento
foreign key (medicamento_id)
references medicamento(id)
on delete set null;
alter table aplicacion drop column nombre;

-- SERVICIO
create table servicio (
    id int auto_increment primary key,
    nombre varchar(100) not null
);

-- DETALLE_ATENCION
create table detalle_atencion (
    id int auto_increment primary key,
    atencion_id int not null,
    servicio_id int not null,

    foreign key (atencion_id) references atencion(id)
        on delete cascade,
    foreign key (servicio_id) references servicio(id)
);

-- ESPECIE
create table especie (
    id int auto_increment primary key,
    nombre varchar(50) not null
);

-- RAZA
create table raza (
    id int auto_increment primary key,
    nombre varchar(50) not null,
    especie_id int,

    foreign key (especie_id) references especie(id)
        on delete cascade
);

alter table mascota
add especie_id int,
add raza_id int;
alter table mascota
add constraint fk_mascota_especie
foreign key (especie_id)
references especie(id);
alter table mascota
add constraint fk_mascota_raza
foreign key (raza_id)
references raza(id);

alter table mascota drop column especie;
alter table mascota drop column raza;
alter table mascota drop column especie_otro;

