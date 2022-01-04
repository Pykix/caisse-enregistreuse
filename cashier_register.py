# reste a faire (je crois):
# - gestion des erreurs de la part de l'utilisateur
# - ajouter les produits manquant
# - changer les choses que vous n'avez pas vu en cours
# - changer le nom des variables


class Produit:
    """
    Classe pour la creation de produit
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructeur qui prend en parametre un dictionnaire pour créer plus clairement
        les instances en passant un dictionnaire dans le constructeur
        """
        self.nom = kwargs.get('nom')
        self.prix_u = kwargs.get('prix_u')
        self.quantite = kwargs.get('qte')

    def __str__(self) -> str:
        """Retourne une string qui permet d'identifier plus simplement l'instance

        Returns:
            str: raw string avec les données relative a l'instance
        """
        return f"{self.nom} : {self.prix_u} eur/u | {self.quantite} en stock"


class Caisse:
    """class qui sert de gestion de stock et de module de facturation
    """

    def __init__(self, liste_articles) -> None:
        """Constructeur qui prend la liste des article pour les ajouter au stock
        ainsi que le panier et le total de la commande

        Args:
            liste_articles (List): contient la liste des produits en stock
        """
        self.liste_produits = liste_articles
        self.panier = {}
        self.total = 0

    def afficher_menu(self):
        """
        Affiche le menu du programme
        """
        print("""
            1. ajouter un article a mon panier
            2. voir mon panier
            3. quitter le magasin
            """)

    def afficher_stock(self):
        """Affiche la list du stock 
        """
        for item in self.liste_produits:
            print(item)

    def ajouter_au_panier(self):
        """ajoute au panier l'item demandé par l'utilisateur,
        crée une clé dans le dictionnaire avec le produit, sa qte et sont prix
        """
        item = input('que voulez-vous ajouter dans votre panier ? ')
        produits = [produit.nom for produit in self.liste_produits]
        if item in produits:
            for article in self.liste_produits:
                if item == article.nom:
                    qte = int(input('combien en voulez vous ? '))
                    article.quantite -= qte
                    self.panier.update(
                        {
                            article.nom: {
                                "qte": qte,
                                "prix_u": article.prix_u,
                                "prix": article.prix_u * qte
                            }
                        }
                    )
            print(self.panier)
        else:
            print("désolé je ne reconnais pas cet article")

    def afficher_panier(self):
        """Affiche le contenu du panier et son montant
        """
        for key, value in self.panier.items():
            print(
                f"{key} | qte : {value.get('qte')} | prix unitaire : {value.get('prix_u')} | total :{value.get('prix')}$"
            )
            self.total += value.get('prix')
        print(f"note totale : {self.total}$")

    def start(self):
        """Démarre le programme
        """
        exit = False
        while not exit:
            self.afficher_menu()
            choix_utilisateur = int(input('que voulez-vous faire ? '))
            if choix_utilisateur == 1:
                self.afficher_stock()
                self.ajouter_au_panier()
            elif choix_utilisateur == 2:
                self.afficher_panier()
            elif choix_utilisateur == 3:
                exit = True
            else:
                print("Je n'ai pas compris votre choix")


# Liste des articles qui vont être mis en stock
articles = [
    {
        "nom": "pain",
        "prix_u": 1,
        "qte": 50
    },
    {
        "nom": "eau",
        "prix_u": 0.5,
        "qte": 40
    },
    {
        "nom": "riz",
        "prix_u": 0.75,
        "qte": 60
    }
]
# Création de la liste de produit avec une comprehension de liste
liste_de_produits = [Produit(**article) for article in articles]

# Initialisation de la caisse en ajoutant les produits en stock
caisse = Caisse(liste_de_produits)

# On demarre la caisse
caisse.start()
