# Script para iniciar Flask automaticamente
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "    🚀 Iniciando aplicacion Flask" -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Navegar al directorio correcto
Write-Host "📁 Navegando al directorio Flask..." -ForegroundColor Green
Set-Location "C:\Users\gagge\OneDrive\Escritorio\Python\Python\Flask"

# Verificar que el archivo existe
if (Test-Path "run.py") {
    Write-Host "✅ Archivo run.py encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ Error: No se encontro run.py" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "🐍 Iniciando servidor Flask..." -ForegroundColor Blue
Write-Host ""
Write-Host "🌐 La aplicacion estara disponible en:" -ForegroundColor Yellow
Write-Host "   http://localhost:5000" -ForegroundColor White
Write-Host "   http://127.0.0.1:5000" -ForegroundColor White
Write-Host ""
Write-Host "💡 Para detener el servidor presiona Ctrl+C" -ForegroundColor Magenta
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Iniciar Flask
python run.py