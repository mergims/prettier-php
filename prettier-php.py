import sublime
import sublime_plugin
import os
import subprocess

dist_dir = os.path.dirname(os.path.abspath(__file__))

class PrettierPhpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		s = sublime.load_settings('prettier-php.sublime-settings')
		php_bin = s.get("php_bin", "php")
		fileName = self.view.file_name()
		dirPath = os.path.dirname(os.path.realpath(__file__))

		subprocess.call([
			'php', 
			php_bin,
			'fix',
			fileName,
			'--rules=@Symfony'
		], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dirPath, shell=False)