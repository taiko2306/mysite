{% extends 'base.html' %}

{% block content %}
    <h2>Secret Page</h2>
    <p>Welcome
        {% if user.is_authenticated %}
           <strong> {{ user.username | capfirst }} </strong>
        , you are now in your own membership page.
        {% else %}
            You should not get here if you are not logged in.
        {% endif %}
    </p>
    <h2>Your Profile</h2>
<p>First Name: <strong>{{ user.first_name}}</strong></p>
    <p>Last Name: <strong>{{ user.last_name}}</strong></p>
    <p>Email: <strong>{{ user.email}}</strong></p>
{% endblock %}