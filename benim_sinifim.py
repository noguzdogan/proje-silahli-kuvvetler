class SilahliKuvvetler(object):  
    "This class represents Silahlı Kuvvetler and it's the parent class.-Oğuz-"
    def Description(self):
        print("Türk Silahlı Kuvvetleri, Türkiye'yi karadan, havadan ve denizden gelebilecek her türlü saldırıya karşı korumakla görevli olan askerî kuvvettir.\n")
        print("Yaptırım gücünü Türkiye Cumhuriyeti Anayasası'ndan alır.\n")
        print("Türk Kara Kuvvetleri, Türk Hava Kuvvetleri ve Türk Deniz Kuvvetlerinden oluşmaktadır.")
    def __init__(self,name,yearOfStart):  
        self.name = name  
        self.yearOfStart = yearOfStart  
    def IsRetired(self):  
        from datetime import datetime           # Anlık seneyi kullanabilmek için datetime modülünü import ettik.  
        instanceTime = datetime.now()           # (init’e almadık ki sürekli import etmeyip  
                                                # gerektiği zamanlarda import etsin, performansta düşüklük yaşamayalım.)  
        if (instanceTime.year - self.yearOfStart) > 40:  
            return True                         # If it's achieved to condition we retire them  
        else:  
            return False  

