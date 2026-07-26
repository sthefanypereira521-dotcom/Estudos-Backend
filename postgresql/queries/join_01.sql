SELECT 
  a.nome,
  c.nome_cursos,
  m.ativo
FROM matriculas m
JOIN alunos a 
  ON a.id = m.aluno_id
JOIN cursos c 
  ON c.id = m.curso_id;

