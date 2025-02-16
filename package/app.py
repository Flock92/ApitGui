from PyQt6.QtWidgets import (
    QWidget, QPushButton, QSpinBox, QRadioButton,
    QCheckBox, QHBoxLayout, QVBoxLayout, QLabel,
    QTimeEdit, QFrame, QScrollArea, QPlainTextEdit,
    QLayout, QLineEdit, QSizePolicy, QComboBox, QListWidget,
    QListWidgetItem, QInputDialog, QFormLayout, QGroupBox,
    QDoubleSpinBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize


class OrderForm(QGroupBox):

    def __init__(self) -> None:
        self.widget = Widgets()

    def updateForm(self) -> None:
        
        # GET TICKER SETTINGS

        # update form and limits
        self.orderPrice.setValue(235)

        self.orderSize.setMinimum(0.5)
        self.orderSize.setMaximum(19000)

        self.tp.setMaximum(5)
        self.tp.setMinimum(5)

        self.sl.setMaximum(3)
        self.sl.setMinimum(3)

    def getData(self) -> dict:

        data = {
            "direction": self.orderType.currentText(),
            "ticker": self.tickerSymbol.text(),
            "orderPrice": self.orderPrice.text(),
            "stopLoss": self.sl.text(),
            "takeProfit": self.tp.text(),
            "slippage": self.slippage.text()
        }

        return data
    
    def quickOrderForm(self, objName: str) -> QGroupBox:

        frame = QGroupBox("Order Form")
        frame.setObjectName(objName)
        form = QFormLayout(frame)

        infoFont = QFont()
        infoFont.setPixelSize(12)

        # Order form
        directionLabel = self.widget.label("Direction\t:")
        directionLabel.setFont(infoFont)
        directionLabel.setStyleSheet("color: grey")

        tradeType = ["Buy", "Sell"]
        self.orderType = self.widget.dropDown()
        self.orderType.setObjectName("quickOrder-Direction")
        self.orderType.addItems(tradeType)

        form.addRow(directionLabel, self.orderType)

        tickerLabel = self.widget.label("Instrument\t:")
        tickerLabel.setFont(infoFont)
        tickerLabel.setStyleSheet("color: grey")
        
        self.tickerSymbol = self.widget.textInput()
        self.tickerSymbol.setPlaceholderText("Enter Ticker (e.g., TSLA, AAPL)")
        self.tickerSymbol.setObjectName("quickOrder-ticker")

        form.addRow(tickerLabel, self.tickerSymbol)

        # Target price
        priceLabel = self.widget.label("OrderPrice\t:")
        priceLabel.setFont(infoFont)
        priceLabel.setStyleSheet("color: grey")

        self.orderPrice = self.widget.dSpinBox()
        self.orderPrice.setMaximum(999999)
        self.orderPrice.setObjectName("quickOrder-orderPrice")

        form.addRow(priceLabel, self.orderPrice)

        # Stoploss target
        slLabel = self.widget.label("StopLoss\t:")
        slLabel.setFont(infoFont)
        slLabel.setStyleSheet("color: grey")

        self.sl = self.widget.dSpinBox()
        self.sl.setMaximum(999999)
        self.sl.setObjectName("quickOrder-stopLoss")

        form.addRow(slLabel, self.sl)

        # takeProfit target
        tpLabel = self.widget.label("TakeProfit\t:")
        tpLabel.setFont(infoFont)
        tpLabel.setStyleSheet("color: grey")

        self.tp = self.widget.dSpinBox()
        self.tp.setMaximum(999999)
        self.tp.setObjectName("quickOrder-takeProfit")

        form.addRow(tpLabel, self.tp)

        # order size (WILL NEED TO GET ORDER LIMIT FROM THE SETTINGS CALL)
        sizeLabel = self.widget.label("Order Size\t:")
        sizeLabel.setFont(infoFont)
        sizeLabel.setStyleSheet("color: grey")

        self.orderSize = self.widget.dSpinBox()
        self.orderSize.setMaximum(999999)
        self.orderSize.setObjectName("quickOrder-orderSize")

        form.addRow(sizeLabel, self.orderSize)

        # slippage
        slippageLabel = self.widget.label("Slippage\t:")
        slippageLabel.setFont(infoFont)
        slippageLabel.setStyleSheet("color: grey")

        self.slippage = self.widget.dSpinBox()
        self.slippage.setSuffix("%")
        self.slippage.setMaximum(999)
        self.slippage.setObjectName("quickOrder-slippage")

        form.addRow(slippageLabel, self.slippage)

        frame.setLayout(form)

        return frame
    
    def autoTraderTickerForm(self, objName: str) -> QFrame:

        frame = QGroupBox("Order Form")
        frame.setObjectName(objName)
        form = QFormLayout(frame)

        



class Form(QFrame):

    def __init__(self, parent, form_name: str):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setObjectName(form_name)

    def form(self) -> QFrame:
        return self
    
    def layout(self) -> QVBoxLayout:
        return super().layout()


class Widgets:

    default_height = 25
    default_font = QFont()
    default_font.setFamilies(["Calibri"])
    default_font.setPixelSize(15)

    def __init__(self) -> None:
        """"""

    def frame(self) -> QFrame:
        widget = QFrame()
        widget.layout = QVBoxLayout()
        widget.setLayout(widget.layout)
        return widget
    
    def hFrame(self) -> QFrame:
        widget = QFrame()
        widget.layout = QHBoxLayout()
        widget.setLayout(widget.layout)
        return widget

    def buttons(self, text: str) -> QPushButton:
        widget = QPushButton()
        widget.setText(text)
        widget.setFixedHeight(self.default_height)
        widget.setFont(self.default_font)
        return widget 
    
    def textInput(self) -> QLineEdit:
        widget = QLineEdit()
        widget.setFixedHeight(self.default_height)
        widget.setFrame(False)
        return widget
    
    def checkBox(self, text: str = None) -> QCheckBox:
        widget = QCheckBox()
        if text:
            widget.setText(text)
        return widget
    
    def label(self, text: str = None) -> QLabel:
        widget = QLabel()
        if text != None:
            widget.setText(text)
        widget.setFont(self.default_font)
        return widget
    
    def scrollArea(self) -> QScrollArea:
        widget = QScrollArea()
        return widget

    def dropDown(self) -> QComboBox:
        widget = QComboBox()
        return widget

    def spinBox(self) -> QSpinBox:
        widget = QSpinBox()
        return widget
    
    def dSpinBox(self) -> QDoubleSpinBox:
        widget = QDoubleSpinBox()
        return widget
    
    def listWidget(self) -> QListWidget:
        widget = QListWidget()
        return widget
    
    def hLine(self) -> QWidget:
        widget = QWidget()
        widget.setFixedHeight(2)
        widget.setStyleSheet("background-color: rgba(128,128,128,0.1)")
        widget.setContentsMargins(5,0,5,0)
        return widget
    
    def inputDialog(self) -> QInputDialog:
        widget = QInputDialog()
        return widget


class CenterWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.widget = Widgets()
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Add title and information to the top of the window
        title_info = self.title_information()
        self.layout.addWidget(title_info)

        # Add connection form to the window
        connection_form = self.connect_form()
        self.layout.addWidget(connection_form)

        self.layout.addWidget(self.widget.hLine()) # Add hor line

        # Add scroll area for options
        options = self.optionsScroll()
        self.layout.addWidget(options[0])

        # Add quicktrade option
        quickTrade = self.quickOrder()
        options[1].layout.addWidget(quickTrade)

        options[1].layout.addWidget(self.widget.hLine()) # Add hor line

        # Add Auto trader settings (allows users to set parameters in a trade loop)
        autoTrader = self.autoTrader()
        options[1].layout.addWidget(autoTrader)

        options[1].layout.addWidget(self.widget.hLine()) # Add hor line

        # Add OpenOrder menu
        openOrders = self.activeOrders()
        options[1].layout.addWidget(openOrders)

    def title_information(self) -> QFrame:

        title_font = QFont()
        title_font.setPixelSize(20)

        info_font = QFont()
        info_font.setPixelSize(12)

        frame = self.widget.frame()
        frame.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        frame.layout.setContentsMargins(0,0,0,0)

        hsplit = self.widget.hFrame()
        hsplit.layout.setContentsMargins(0,10,0,0)
        hsplit.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_title = self.widget.label("ApitConnect")
        main_title.setFont(title_font)
        main_title.setAlignment(Qt.AlignmentFlag.AlignBottom)
        hsplit.layout.addWidget(main_title)

        info = self.widget.label("Connect to Apit extension.")
        info.setFont(info_font)
        info.setStyleSheet("color: grey")
        info.setAlignment(Qt.AlignmentFlag.AlignBottom)
        hsplit.layout.addWidget(info)

        frame.layout.addWidget(hsplit)

        return frame

    def connect_form(self) -> QFrame:
        """"""

        status_font = QFont()
        status_font.setPixelSize(11)

        frame = self.widget.frame()
        frame.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        frame.layout.setContentsMargins(0,0,0,0)

        # Create The form container
        connect_form = Form(self, "connect")
        connect_form.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        connect_form.setContentsMargins(0,0,0,0)
        connect_form.setMaximumHeight(200)

        titleH = self.widget.hFrame()
        titleH.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        connect_form.layout.addWidget(titleH)

        label = self.widget.label("Connection Settings") 
        label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        titleH.layout.addWidget(label)

        status_label = self.widget.label()
        status_label.setFont(status_font)
        status_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.updateStatus(status_label)
        titleH.layout.addWidget(status_label)
        
        host_input = self.widget.textInput()
        host_input.setPlaceholderText("Enter host (e.g., localhost)")
        connect_form.layout.addWidget(host_input)

        port_input = self.widget.textInput()
        port_input.setPlaceholderText("Enter port (e.g., 8765)")
        connect_form.layout.addWidget(port_input)

        hSplit = self.widget.hFrame()
        hSplit.layout.setContentsMargins(0,0,0,0)
        connect_form.layout.addWidget(hSplit)

        connect_btn = self.widget.buttons("RunServer")
        connect_btn.setFixedWidth(90)
        hSplit.layout.addWidget(connect_btn)

        frame.layout.addWidget(connect_form)
        self.layout.addWidget(frame)

    def updateStatus(self, label: QLabel) -> None:
        """change color of text"""

        connected = False
        status_colors = ["red","green"]

        if connected:
            label.setText("Server up")
            label.setStyleSheet(f"color: {status_colors[1]}")
        else:
            label.setText("Server down")
            label.setStyleSheet(f"color: {status_colors[0]}")

    def optionsScroll(self) -> QScrollArea:

        titleFont = QFont()
        titleFont.setPixelSize(19)

        frame = self.widget.frame()
        frame.layout.setContentsMargins(0,0,0,0)

        # optTitle = self.widget.label("Options")
        # optTitle.setContentsMargins(10,0,0,0)
        # optTitle.setFont(titleFont)
        # frame.layout.addWidget(optTitle)

        scrollArea = self.widget.scrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameStyle(0)
        frame.layout.addWidget(scrollArea)

        container = self.widget.frame()
        container.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scrollArea.setWidget(container)

        return [frame, container]
    
    def quickOrder(self) -> QFrame:

        form = OrderForm()

        infoFont = QFont()
        infoFont.setPixelSize(12)

        frame = self.widget.frame()
        frame.layout.setContentsMargins(0,0,0,0)

        # Option title and information
        label = self.widget.label("QuickTrade")
        frame.layout.addWidget(label)

        infoLabel = self.widget.label("submit or create quick order buttons.")
        infoLabel.setFont(infoFont)
        infoLabel.setStyleSheet("color: grey")
        frame.layout.addWidget(infoLabel)

        quickOrderForm = form.quickOrderForm("quickOrderGroup")
        frame.layout.addWidget(quickOrderForm) # TEST --------------------------------

        # Display simple information about the trade (Total order price, stoploss and takeprofit price and margin price)
        orderInfoFont = QFont()
        orderInfoFont.setPixelSize(10)

        orderInfoSpan = self.widget.hFrame()
        orderInfoSpan.layout.setContentsMargins(0,0,0,0)
        frame.layout.addWidget(orderInfoSpan)

        orderTotalLabel = self.widget.label("tot:")
        orderTotalLabel.setFont(orderInfoFont)
        orderTotalLabel.setStyleSheet("color: grey")
        orderInfoSpan.layout.addWidget(orderTotalLabel)

        orderTotal = self.widget.textInput()
        orderTotal.setReadOnly(True)
        orderInfoSpan.layout.addWidget(orderTotal)

        stopLossPriceLabel = self.widget.label("SL:")
        stopLossPriceLabel.setFont(orderInfoFont)
        stopLossPriceLabel.setStyleSheet("color: grey")
        orderInfoSpan.layout.addWidget(stopLossPriceLabel)

        stopLoss = self.widget.textInput()
        stopLoss.setReadOnly(True)
        orderInfoSpan.layout.addWidget(stopLoss)

        takeProfitPriceLabel = self.widget.label("TP:")
        takeProfitPriceLabel.setFont(orderInfoFont)
        takeProfitPriceLabel.setStyleSheet("color: grey")
        orderInfoSpan.layout.addWidget(takeProfitPriceLabel)

        takeProfit = self.widget.textInput()
        takeProfit.setReadOnly(True)
        orderInfoSpan.layout.addWidget(takeProfit)

        depositPriceLabel = self.widget.label("dep:")
        depositPriceLabel.setFont(orderInfoFont)
        depositPriceLabel.setStyleSheet("color: grey")
        orderInfoSpan.layout.addWidget(depositPriceLabel)

        depositPrice = self.widget.textInput()
        depositPrice.setReadOnly(True)
        orderInfoSpan.layout.addWidget(depositPrice)

        # Submit or Create order button
        submitBtn = self.widget.buttons("Submit")   # Submit order
        frame.layout.addWidget(submitBtn)

        createbtn = self.widget.buttons("Create")   # Create a quick fire button
        frame.layout.addWidget(createbtn)

        # Link function to buttons
        submitBtn.clicked.connect(lambda x: self.submitOrder(form.getData()))
        createbtn.clicked.connect(lambda x: self.createOrderShortcut(form.getData()))

        # Setup listeners
        form.tickerSymbol.editingFinished.connect(lambda: print(form.updateForm())) # Run a function that gets information about the ticker

        return frame
    
    def submitOrder(self, data) -> None:
        print(data)

        # Need function to send order
    
    def createOrderShortcut(self, data) -> None:
        print(data)

        # Needs function to create button or order card
    
    def activeOrders(self) -> QFrame:

        infoFont = QFont()
        infoFont.setPixelSize(12)
        
        frame = self.widget.frame()
        frame.layout.setContentsMargins(0,0,0,0)

        # Option title and information
        label = self.widget.label("ActiveOrders")
        frame.layout.addWidget(label)

        infoLabel = self.widget.label("current active positions.")
        infoLabel.setFont(infoFont)
        infoLabel.setStyleSheet("color: grey")
        frame.layout.addWidget(infoLabel)

        # contatiner for list of positions
        postionList = self.widget.listWidget()
        postionList.addItem("TSLA")
        postionList.addItem("AAPL")
        postionList.addItem("META")
        postionList.addItem("BT")

        frame.layout.addWidget(postionList)

        # Refresh button allow user to get
        refreshBtn = self.widget.buttons("Refresh")
        frame.layout.addWidget(refreshBtn)

        return frame
        
    def autoTrader(self) -> QFrame:

        infoFont = QFont()
        infoFont.setPixelSize(12)

        frame = self.widget.frame()
        frame.layout.setContentsMargins(0,0,0,0)

        # Option title and information
        label = self.widget.label("AutoTrader")
        frame.layout.addWidget(label)

        infoLabel = self.widget.label("Set params for 'AutoTrader'.")
        infoLabel.setFont(infoFont)
        infoLabel.setStyleSheet("color: grey")
        frame.layout.addWidget(infoLabel)

        tickersH = self.widget.hFrame()
        tickersH.layout.setContentsMargins(0,0,0,0)
        frame.layout.addWidget(tickersH)

        # Add ticker to autotrader
        tickerList = self.widget.listWidget()
        tickersH.layout.addWidget(tickerList)

        # list buttons container
        tickerListBtns = self.widget.frame()
        tickerListBtns.layout.setContentsMargins(0,0,0,0)
        tickersH.layout.addWidget(tickerListBtns)

        addTickerButton = self.widget.buttons("Add")
        tickerListBtns.layout.addWidget(addTickerButton)

        removeTickerButton = self.widget.buttons("Remove")
        tickerListBtns.layout.addWidget(removeTickerButton)

        clearTickerButton = self.widget.buttons("Clear")
        tickerListBtns.layout.addWidget(clearTickerButton)

        self.autoTrader_addTicker(tickerList)


        return frame
    
    def autoTrader_addTicker(self, list: QListWidget) -> QListWidgetItem:

        tickerDialog = self.widget.inputDialog()
        return tickerDialog
