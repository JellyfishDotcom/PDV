from abc import ABCMeta, abstractclassmethod

class Window(metaclass=ABCMeta):
    @abstractclassmethod
    def _on_closing(self):
        pass
    
    @abstractclassmethod
    def _init_frames(self):
        pass

    @abstractclassmethod    
    def _init_figures(self):
        pass

    @abstractclassmethod
    def _init_buttons(self):
        pass

    @abstractclassmethod
    def _init_labels(self):
        pass

    @abstractclassmethod
    def _init_entrys(self):
        pass

    @abstractclassmethod
    def init_comp(self):
        pass