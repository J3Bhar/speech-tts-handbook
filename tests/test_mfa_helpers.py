"""Synthetic-only MFA helper tests; no datasets or server access."""
import importlib.util
import tempfile
import unittest
import wave
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(name):
    spec=importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name+".py"))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class MFATest(unittest.TestCase):
    def test_prepare_and_check(self):
        with tempfile.TemporaryDirectory() as root:
            d=Path(root)
            source=d/"source.wav"
            with wave.open(str(source),"wb") as f:
                f.setnchannels(1);f.setsampwidth(2);f.setframerate(16000)
                f.writeframes(b"\x00\x00"*100)
            manifest=d/"input.tsv"
            manifest.write_text("example_001\tsource.wav\tHello world\tspeaker_001\n",encoding="utf-8")
            out=d/"prepared"
            n=load("mfa_prepare").prepare(manifest,out)
            self.assertEqual(n,1)
            c,errors=load("mfa_check_corpus").check_corpus(out)
            self.assertEqual((c,errors),(1,[]))
            self.assertTrue(source.is_file())
            with self.assertRaises(ValueError):
                load("mfa_prepare").prepare(manifest,out)
    def test_invalid_manifest(self):
        with tempfile.TemporaryDirectory() as root:
            d=Path(root)
            manifest=d/"input.tsv"
            manifest.write_text("bad id\tmissing.wav\twords\n",encoding="utf-8")
            with self.assertRaises(ValueError):
                load("mfa_prepare").prepare(manifest,d/"prepared",True)

if __name__=="__main__":
    unittest.main()
