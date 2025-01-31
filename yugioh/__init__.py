import requests

# Important variables
base_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
monsters = ["Effect Monster", "Flip Effect Monster", "Flip Tuner Effect Monster", "Gemini Monster", "Normal Monster", "Normal Tuner Monster", "Pendulum Effect Monster", "Pendulum Flip Effect Monster", "Pendulum Normal Monster", "Pendulum Tuner Effect Monster", "Ritual Effect Monster", "Ritual Monster", "Spirit Monster", "Toon Monster", "Tuner Monster", "Union Effect Monster", "Fusion Monster", "Pendulum Effect Fusion Monster", "Synchro Monster", "Synchro Pendulum Effect Monster", "Synchro Tuner Monster", "XYZ Monster", "XYZ Pendulum Effect Monster"]
specials = ["Skill Card", "Spell Card", "Trap Card"]
link = "Link Monster"

# Get a card by typing an exact name or id
class get_card:
    def __init__(self, card_name=None, card_id=None):
        if card_name is not None:
            parameters = {'name':card_name}
            card_id == None
        if card_id is not None:
            parameters = {'id':card_id}
        card = requests.get(base_url, params=parameters).json()
        self.description = card['data'][0]['desc']
        self.id = card['data'][0]['id']
        self.name = card['data'][0]['name']
        self.race = card['data'][0]['race']
        self.type = card['data'][0]['type']
        self.cardmarket_price = card['data'][0]['card_prices'][0]['cardmarket_price']
        self.tcgplayer_price = card['data'][0]['card_prices'][0]['tcgplayer_price']
        self.ebay_price = card['data'][0]['card_prices'][0]['ebay_price']
        self.amazon_price = card['data'][0]['card_prices'][0]['amazon_price']
        self.coolstuffinc_price = card['data'][0]['card_prices'][0]['coolstuffinc_price']
        if self.type in monsters:
            self.attack = card['data'][0]['atk']
            self.attribute = card['data'][0]['attribute']
            self.defense = card['data'][0]['def']
            self.level = card['data'][0]['level']
        try:
            self.archetype = card['data'][0]['archetype']
        except:
            self.archetype = None
        if self.type == link:
            self.attack = card['data'][0]['atk']
            self.attribute = card['data'][0]['attribute']
            self.defense = None
            self.linkmarkers = card['data'][0]['linkmarkers']
            self.linkval = card['data'][0]['linkval']
        if self.type in specials:
            self.defense = None

# Get card list with similar names to the one typed.
class get_cards_by_name:
    def __init__(self, keyword):
        parameters = {'fname':keyword}
        cards = requests.get(base_url, params=parameters).json()
        self.list = [card['name'] for card in cards['data']]

# Get list with cards in the banlist and it's banlist status (limited, semi, forbidden).
# Example usage: print(card.list[0][1]['ban_tcg'])
class get_banlist:
    def __init__(self, banlist):
        parameters = {'banlist':banlist}
        cards = requests.get(base_url, params=parameters).json()
        self.list = []
        for card in cards['data']:
            auxList = []
            auxList.append(card['name'])
            auxList.append(card['banlist_info'])
            self.list.append(auxList)

