function updateSkills() {
    var professionSkills = {
        {% for position, skill in skills_dict.items %}
            '{{ position }}': {{ skill|safe }},
        {% endfor %}
    };

    var jobPositionSelect = document.getElementById('id_job_position');
    var selectedPosition = jobPositionSelect.options[jobPositionSelect.selectedIndex].value;
    var requiredSkillsField = document.getElementById('id_required_skills');
    requiredSkillsField.innerHTML = ''; // Clear previous options

    var skills = professionSkills[selectedPosition];
    if (skills) {
        for (var i = 0; i < skills.length; i++) {
            var option = document.createElement('option');
            option.text = skills[i];
            option.value = skills[i];
            requiredSkillsField.add(option);
        }
    }
}