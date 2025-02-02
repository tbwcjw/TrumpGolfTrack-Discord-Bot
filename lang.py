import config

# Translations may be inaccurate.
# I may be a lot of things but multilingual is not one of them.
# Fix Google Translates mistakes, and add new languages.
# https://github.com/tbwcjw/TrumpGolfTrack-Discord-Bot

def i8ln(key):
    return translations.get(config.LANG, {}).get(key, translations[config.LANG].get(key, key))

translations = {
    "en": {
        "track_description": "Get statistics about Trumps Golfing activities",
        "track_title": "Donald Trump Golf Tracker",
        "days_until": "Days until next Presidency",
        "days": "days",
        "provided_by": "Data provided by",
        "non_affiliate": "a nonaffiliate",
        "days_in_office": "Days in Office",
        "president_since": "President Since",
        "days_spent_golfing": "Days Spent Golfing",
        "perc_spent_golfing": "Percentage of Presidency spent Golfing",
        "days_golfed_on": "Days Golfed on"
    },
    "es": {
        "track_description": "Obtén estadísticas sobre las actividades de golf de Trump",
        "track_title": "Rastreador de Golf de Donald Trump",
        "days_until": "Días hasta la próxima presidencia",
        "days": "días",
        "provided_by": "Datos proporcionados por",
        "non_affiliate": "un no afiliado",
        "days_in_office": "Días en el cargo",
        "president_since": "Presidente desde",
        "days_spent_golfing": "Días pasados jugando al golf",
        "perc_spent_golfing": "Porcentaje de la presidencia dedicado al golf",
        "days_golfed_on": "Días jugados al golf"
    },
    "fr": {
        "track_description": "Obtenez des statistiques sur les activités de golf de Trump",
        "track_title": "Suivi du golf de Donald Trump",
        "days_until": "Jours jusqu'à la prochaine présidence",
        "days": "jours",
        "provided_by": "Données fournies par",
        "non_affiliate": "un non affilié",
        "days_in_office": "Jours en fonction",
        "president_since": "Président depuis",
        "days_spent_golfing": "Jours passés à jouer au golf",
        "perc_spent_golfing": "Pourcentage de la présidence passé à jouer au golf",
        "days_golfed_on": "Jours joués au golf"
    }
}

