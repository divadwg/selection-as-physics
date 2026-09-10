"""Physical balances for binary material and fractional reflection."""
import unittest
import numpy as np
from sims.validation.material import Material, bonds, exchange_gain, reflect
from sims.boundaries.lg import cx, cy, opp


class MaterialTests(unittest.TestCase):
    def test_exchange_energy_against_whole_grid(self):
        rng = np.random.default_rng(12)
        for _ in range(100):
            bits = rng.random((7, 8)) < .5
            x, y, axis = int(rng.integers(7)), int(rng.integers(8)), int(rng.integers(2))
            gain = exchange_gain(bits, x, y, axis); before = bonds(bits)
            xx, yy = ((x+1) % 7, y) if axis == 0 else (x, (y+1) % 8)
            bits[x, y], bits[xx, yy] = bits[xx, yy], bits[x, y]
            self.assertEqual(bonds(bits)-before, gain)

    def test_relaxation_conserves_material_and_lowers_energy(self):
        material = Material(np.random.default_rng(9).random((24, 32)) < .4)
        initial = material.bits.sum(); previous = bonds(material.bits)
        for _ in range(20):
            material.sweep()
            self.assertEqual(material.bits.sum(), initial)
            self.assertGreaterEqual(bonds(material.bits), previous)
            previous = bonds(material.bits)
            self.assertAlmostEqual(material.coarse().sum()*16, initial)

    def test_reflection_conserves_mass_and_accounts_for_momentum(self):
        rng = np.random.default_rng(7); f = rng.random((9, 8, 10)); s = rng.random((8, 10))
        out = reflect(f, s)
        np.testing.assert_allclose(out.sum(0), f.sum(0), atol=1e-14)
        for c in (cx, cy):
            np.testing.assert_allclose((out*c[:, None, None]).sum(0),
                                       (1-2*s)*(f*c[:, None, None]).sum(0), atol=1e-14)
        np.testing.assert_array_equal(reflect(f, np.zeros_like(s)), f)
        np.testing.assert_array_equal(reflect(f, np.ones_like(s)), f[opp])


if __name__ == '__main__':
    unittest.main()
