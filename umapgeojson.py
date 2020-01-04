import json
import geojson

class uMapProperties:
    """
    uMapに登録した地物をGeoJSON形式にした際propertiesに登録される情報を保持するクラス
    """
    def __init__(self, name = None, desc = None, color = 'Yellow', showLabel = None, iconUrl = None):
        """
        Parameters
        ----------
        name : 地物の名称、ラベルとして表示される
        desc : 地物の概要、地物をクリックした際にラベルとともに表示される
        color : シェイプ表示プロパティの色
        showLabel : ???（いつもnullが指定されている）
        iconUrl : 表示するアイコンシンボルファイルのURL
        """
        self.name = name
        self.desc = desc
        self.color = color
        self.showLabel = showLabel
        self.iconUrl = iconUrl

    def getDict(self):
        """
        地物のpropeties情報をDict形式で返す
        Returns
        -------
        properties : dict
            地物のproperties情報
        """
        _umap_options=dict()
        _umap_options['color']=self.color
        _umap_options['showLabel']=self.showLabel
        if self.iconUrl is not None:
            _umap_options['iconUrl']=self.iconUrl
        properties=dict()
        properties['_umap_options'] = _umap_options
        properties['name'] = self.name
        properties['description'] = self.desc
        return properties
    
    def getJSON(self):
        """
        地物のpropeties情報をJSON形式で返す
        Returns
        -------
        text : json
            地物のproperties情報
        """
        text = json.dumps(self.getDict())
        return text

class uMapFeature:
    """
    uMap用Featureの情報を保持するクラス
    """
    def __init__(self, longitude, latitude, name, desc, color, showLabel, iconUrl):
        """
        Parameters
        ----------
        longitude : 地物の名称、ラベルとして表示される
        latitude : 地物の概要、地物をクリックした際にラベルとともに表示される
        """
        self.longitude = longitude
        self.latitude = latitude
        self.uMapProperties = uMapProperties(name=name, desc=desc, color=color, showLabel=showLabel,  iconUrl=iconUrl)
    
    def getGeoJSON(self):
        """
        uMap用Featureの情報を保持するGeoJSONオブジェクトを返す
        Returns
        -------
        feature : GeoJSON
            uMap用Featureの情報
        """
        point = geojson.Point((self.longitude, self.latitude))
        umap_prop = self.uMapProperties.getDict()
        feature = geojson.Feature(geometry=point,properties=umap_prop)
        return feature

class ATMFeature(uMapFeature):
    """
    ATMの情報を保持するクラス
    """
    name='ATM'
    desc='店名:\n利用時間:'
    color='Green'
    showLabel=None
    iconUrl='/uploads/pictogram/museum-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, ATMFeature.name, ATMFeature.desc, ATMFeature.color, ATMFeature.showLabel, ATMFeature.iconUrl)

class AEDFeature(uMapFeature):
    """
    AEDの情報を保持するクラス
    """
    name='AED'
    desc='店名:\n利用時間:'
    color='Crimson'
    showLabel=None
    iconUrl='/uploads/pictogram/hospital-24-white.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, AEDFeature.name, AEDFeature.desc, AEDFeature.color, AEDFeature.showLabel, AEDFeature.iconUrl)

class FreeWiFiFeature(uMapFeature):
    """
    FreeWiFiの情報を保持するクラス
    """
    name='FreeWiFi'
    desc='店名:\n利用時間:'
    color='DarkBlue'
    showLabel=None
    iconUrl='/uploads/pictogram/golf-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, FreeWiFiFeature.name, FreeWiFiFeature.desc, FreeWiFiFeature.color, FreeWiFiFeature.showLabel, FreeWiFiFeature.iconUrl)

class SSWHFeature(uMapFeature):
    """
    Support Station for Walking to Home(SSWH)の情報を保持するクラス
    """
    name='災害時帰宅支援ステーション'
    desc='店名:\n利用時間:'
    color='Red'
    showLabel=None
    iconUrl='/uploads/pictogram/school-24-white.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, SSWHFeature.name, SSWHFeature.desc, SSWHFeature.color, SSWHFeature.showLabel, SSWHFeature.iconUrl)

class BenchFeature(uMapFeature):
    """
    ベンチの情報を保持するクラス
    """
    name='ベンチ'
    desc='補足:'
    color='LimeGreen'
    showLabel=None
    iconUrl='/uploads/pictogram/star-24-white.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, BenchFeature.name, BenchFeature.desc, BenchFeature.color, BenchFeature.showLabel, BenchFeature.iconUrl)

class VMFeature(uMapFeature):
    """
    Vending Machine(自動販売機）の情報を保持するクラス
    """
    name='自動販売機'
    desc='種別:\n台数;'
    color='DodgerBlue'
    showLabel=None
    iconUrl='/uploads/pictogram/cafe-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, VMFeature.name, VMFeature.desc,VMFeature.color, VMFeature.showLabel, VMFeature.iconUrl)

class VMADFeature(uMapFeature):
    """
    Vending Machine Available in case of Disaster(災害時利用可能型自動販売機）の情報を保持するクラス
    """
    name='災害対応自動販売機'
    desc='種別:\n台数;'
    color='DodgerBlue'
    showLabel=None
    iconUrl='/uploads/pictogram/cafe-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, VMADFeature.name, VMADFeature.desc, VMADFeature.color, VMADFeature.showLabel, VMADFeature.iconUrl)

class ToiletFeature(uMapFeature):
    """
    トイレの情報を保持するクラス
    """
    name='トイレ'
    desc='種別:\n補足:'
    color='Yellow'
    showLabel=None
    iconUrl='/uploads/pictogram/toilets-24.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        super().__init__(longitude, latitude, ToiletFeature.name, ToiletFeature.desc, ToiletFeature.color, ToiletFeature.showLabel, ToiletFeature.iconUrl)
