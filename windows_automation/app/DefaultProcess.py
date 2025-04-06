from qrlib.QRProcess import QRProcess
from qrlib.QRDecorators import run_item
from qrlib.QRRunItem import QRRunItem
from DefaultComponent import WesbsiteComponent
import logging

class DefaultProcess(QRProcess):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("WikiScraper")
        self.website_component = WesbsiteComponent()
        self.register(self.website_component)
        self.data = []

    @run_item(is_ticket=False)
    def before_run(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)
        try:
            self.website_component.open_website()
        except Exception as e:
            self.logger.error("Error opening website")
            raise e
        
        

    @run_item(is_ticket=False, post_success=False)
    def before_run_item(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)

    @run_item(is_ticket=True)
    def execute_run_item(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)
        try:
            self.website_component.get_data()
            scraped_data = self.website_component.data
            title = scraped_data.get("title")
            title2 = scraped_data.get("title2")
            para1 = scraped_data.get("para1")
            para2 = scraped_data.get("para2")
            para3 = scraped_data.get("para3")
            list_items = scraped_data.get("list_items")

            self.website_component.open_word()
            self.website_component.open_blank_doc()
            self.website_component.write_to_word(title,para1,para2,para3,title2,list_items)
            self.website_component.format_doc()
            self.website_component.save_doc()
        except Exception as e:
            self.logger.error("Error writing in a word")
            raise e

        # self.default_component.test()
        # run_item.report_data["test"] = args[0]

    @run_item(is_ticket=False, post_success=False)
    def after_run_item(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)

    @run_item(is_ticket=False, post_success=False)
    def after_run(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)
        self.website_component.close_word()
        # self.default_component.logout()
 
    def execute_run(self):
        self.execute_run_item()
           

