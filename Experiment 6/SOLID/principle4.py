"""
Interface Segregation Principle
Definition: A client should never be forced to implement an interface that it does not use, or clients should not be forced to depend on methods they do not use.
"""
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class AllInOnePrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

class BasicPrinter(Printer):
    def print_document(self):
        print("Printing document")

# Here the basic printer does not need to implement the scan_document method as it is not required for its functionality

# Usage
aio_printer = AllInOnePrinter()
basic_printer = BasicPrinter()
aio_printer.print_document()
aio_printer.scan_document()
basic_printer.print_document()
