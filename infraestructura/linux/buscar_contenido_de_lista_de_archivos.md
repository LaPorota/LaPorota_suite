    DATO="dato_a_buscar" && for archivo in *; do [[ -f "$archivo" ]] && grep -q "$DATO" "$archivo" && echo "Coincidencia encontrada en: $archivo"; done
