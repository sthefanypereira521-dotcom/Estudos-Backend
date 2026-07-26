tabela aluno 


CREATE TABLE IF NOT EXISTS public.alunos
(
    id integer NOT NULL DEFAULT nextval('alunos_id_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(150) COLLATE pg_catalog."default" NOT NULL,
    ano_nascimento integer,
    CONSTRAINT alunos_pkey PRIMARY KEY (id),
    CONSTRAINT alunos_email_key UNIQUE (email)
)

