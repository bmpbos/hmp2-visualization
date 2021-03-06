###
# Config

debug = False
map_file = "./input/hmp2_pilot_w_16S/map.txt"
diet_data = "./input/hmp2_pilot_w_16S/diet.txt"
products_dir = "products"
database_dir = "/local/ibdmdb/hmp2-visualizations/databases/hmp2_pilot_w_16S"

class web:
    host = "127.0.0.1"
    port = "8765"
    #prefix_url = "/patient" #no prefix by default
    prefix_url = "/participant" 
    static_url_base = "https://ibdmdb.org/static/"
