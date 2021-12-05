import vnpy
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
# from vnpy.gateway.ctp import CtpGateway
# from vnpy_ctptest import CtptestGateway
# from vnpy.gateway.ib import IbGateway
from vnpy.plugin.ib import IbGateway

# from vnpy.app.paper_account import PaperAccountApp
# from vnpy.app.cta_strategy import CtaStrategyApp
# from vnpy.app.cta_backtester import CtaBacktesterApp

from vnpy.app.data_manager import DataManagerApp


def main():
    """Start VN Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # main_engine.add_gateway(CtpGateway)
    # main_engine.add_gateway(CtptestGateway)
    main_engine.add_gateway(IbGateway)

    # main_engine.add_app(PaperAccountApp)
    # main_engine.add_app(CtaStrategyApp)
    # main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(DataManagerApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()

if __name__ == "__main__":
    main()