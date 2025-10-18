.PHONY: formats clean
LINE ?=
formats:
	@[ -n "$(LINE)" ] || (echo "Usage: make formats LINE='C/2025 N1 (ATLAS) …'"; exit 2)
	python tools/3i_elements_to_formats.py --line "$(LINE)"
clean:
	rm -f templates/stellarium/3I_ATLAS_mpc_elements.txt \
	templates/skysafari/3I_ATLAS_mpc_1line.txt \
	templates/kstars/3I_ATLAS_comets_dat_snippet.txt
