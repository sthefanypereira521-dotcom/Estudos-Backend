CREATE TABLE IF NOT EXISTS public.cursos
(
    id integer NOT NULL DEFAULT nextval('cursos_id_seq'::regclass),
    nome_cursos character varying(100) COLLATE pg_catalog."default" NOT NULL,
    carga_hora integer NOT NULL,
    valor numeric(10,2),
    ativo boolean DEFAULT true,
    data_criacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT cursos_pkey PRIMARY KEY (id)
)

