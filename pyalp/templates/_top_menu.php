{% load trans %}
{% load spacer %}

		<div align="{{ skin.container.title_menu }}">
            {% spacer 18 %}

            {% if not ALP_TOURNAMENT_MODE %}
    			<a href="index.php" class="menu"><strong>{% trans "home" %}</strong></a>
    		{% endif %}

    		{% if flags.files and not ALP_TOURNAMENT_MODE %}
    			&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>&nbsp;&nbsp;<a href="files.php" class="menu"><strong>{% trans "files" %}</strong></a>
    		{% endif %}

    		{% if flags.seating and not ALP_TOURNAMENT_MODE %}
    			&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>&nbsp;&nbsp;<a href="seating.php" class="menu"><strong>{% trans "map" %}</strong></a>
    		{% endif %}

    		{% if flags.music and not ALP_TOURNAMENT_MODE %}
    			&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>&nbsp;&nbsp;<a href="music.php" class="menu"><strong>{% trans "music" %}</strong></a>
    		{% endif %}

    		{% if flags.schedule %}
    			&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>&nbsp;&nbsp;
    			<a href="disp_schedule.php" class="menu"><strong>{% trans "schedule" %}</strong></a>
    		{% endif %}

            {% if flags.pizza %}
                &nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>
                &nbsp;&nbsp;<a href="pizza.php" class="menu"><strong>{% trans 'pizza' %}</strong></a>
            {% endif %}

    		{% if flags.servers and ALP_TOURNAMENT_MODE_COMPUTER_GAMES %}
    			&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>
                &nbsp;&nbsp;<a href="servers.php" class="menu"><strong>{% trans "servers" %}</strong></a>
            {% endif %}

    		&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>
            &nbsp;&nbsp;<a href="tournaments.php" class="menu"><strong>{% trans "tournaments" %}</strong></a>

            {% if flags.sponsors and not ALP_TOURNAMENT_MODE %}
                &nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>
                &nbsp;&nbsp;<a href="disp_sponsors.php" class="menu"><strong>{% trans "sponsors" %}</strong></a>
            {% endif %}

            {% if not ALP_TOURNAMENT_MODE and flags.staff %}
                &nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>&nbsp;&nbsp;<a href="staff.php" class="menu"><strong>{% trans "staff" %}</strong></a>
            {% endif %}

    		{% if not ALP_TOURNAMENT_MODE %}
    			&nbsp;&nbsp;<font color="{{ skin.colors.blended_text }}">|</font>&nbsp;&nbsp;<a href="users.php" class="menu"><strong>{% trans "users" %}</strong></a>
            {% endif %}

    		{% spacer skin.container.horizontalpadding %}
        </div>
