# test_nodelynxar.py
"""
Tests for NodeLynxar module.
"""

import unittest
from nodelynxar import NodeLynxar

class TestNodeLynxar(unittest.TestCase):
    """Test cases for NodeLynxar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeLynxar()
        self.assertIsInstance(instance, NodeLynxar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeLynxar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
