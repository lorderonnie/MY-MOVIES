class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig:
    '''
    production configuration child class
    
    Args:
        Config: The parent configuration settings 
    '''
    pass

class DevConfig:
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True