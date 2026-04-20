# Choix de l'API

* Étudiant : Hamedy Yahya Camara
* API choisie : Agify
* URL de base : https://api.agify.io
* Documentation officielle : https://agify.io/documentation
* Authentification : Aucune

* Points de terminaison testés :
   * GET https://api.agify.io?name=michael
   * GET https://api.agify.io?name=hamedy

* Hypothèses de contrat (champs attendus, types, codes) :
   * Champ "name" : string
   * Champ "age" : integer
   * Champ "count" : integer
   * Code HTTP attendu : 200

* Limites / limitation de débit connues :
   * 1000 requêtes gratuites par jour sans clé API

* Risques (instabilité, temps d'arrêt, CORS, etc.) :
   * API externe, disponibilité non garantie
   * Résultats basés sur des statistiques, pas toujours précis
