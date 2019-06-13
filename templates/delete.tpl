{% extends 'bootstrap/base.html'%}

{% block styles %}
{{super()}}
     <style>
            h3{background-color:red;color:yellow;}
     </style>
{% endblock %}

{% block content %}
         <form method="POST" action="/marca/del">
               <input type="hidden" name="id" value="{{dados[0]}}"/>
               <p>Nome: {{dados[1]}}</p>
               <p>Origem: {{dados[2]}}</p>
               <p>Presidente: {{dados[3]}}</p>
               <p>Fundacao: {{dados[4]}}</p>
               <input class="btn btn-danger" type ="submit" value ="Deletar"/>
                </form>
{% endblock %}

