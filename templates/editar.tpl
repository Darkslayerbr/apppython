<!DOCTYPE html>
<html lang="pt-BR">
<head>
     <meta charset="UTF-8"/>
     <title>Editar</title>
</head>
<body>
     <h1>Editar</h1>
     <form action="/marca/edit/{{ dados[0] }}" method="POST">
         <p>Nome:<input type="text" name="nome" value="{{ dados[1] }}"/></p>
         <p>presidente:<input type="text" name="presidente" value="{{ dados[2] }}"/></p>
         <p>origem:<input type="text" name="origem" value="{{ dados[3] }}"/></p>
         <p>fundacao:<input type="text" name="fundacao" value="{{ dados[4] }}"/></p>
         <p><input type="submit" value="Gravar"/></p>
     </form>

</body>
</html>
