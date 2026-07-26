SELECT c.nome_cursos, COUNT(*) 
FROM matriculas m
JOIN cursos c ON c.id = m.curso_id
GROUP BY c.nome_cursos;

