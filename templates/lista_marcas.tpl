<DOCTYPE html>
<html lang "pt-BR">
<head>
	<meta charset="UTF-8"/>
	<title>MEU Index</title>
	<a href="/marcas">Lista Marcas</a>
</head>
<body>
	<h1> lista de marcas </h1>
	<a href="/marca/ins">INSERIR</a>
	<table>
	<tr>
		<th> id</th>
		<th>nome</th>
		<th>presidente</th>
		<th>origem</th>
		<th>fundação</th>
		<th>Ações</th>
	<tr>
	{%for dado in dados %}
	<tr>
		<td>{{dado[0]}}</td>
		<td>{{dado[1]}}</td>
		<td>{{dado[2]}}</td>
		<td>{{dado[3]}}</td>
		<td>{{dado[4]}}</td>
		<td> <a href="/marca/edit/{{dado[0]}}">Editar</a> <a href=/marca/view/{{dado[0]}}>Vizualizar</a></td>
		<td> <a href="/marca/del/{{dado[0]}}">Deletar</a> </td>
	</tr>
	{% endfor %}
	</table>
</body>
<html>
