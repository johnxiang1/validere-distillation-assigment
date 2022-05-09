import unittest
from utils import weighted_average_distillation_model


class TestMixture(unittest.TestCase):
    def test_weight_average_function(self):
        result = self.result = weighted_average_distillation_model(v1 = 10, v2 = 30, temperature1 = 35, temperature2 = 100)
        self.assertEqual(result, 83.75)

if __name__ == '__main__':
    unittest.main()
