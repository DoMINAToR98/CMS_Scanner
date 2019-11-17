#!/bin/bash
echo "    ___                       __   "      
echo "   /   |  _____ ___   ____   / /__ ____ _"
echo "  / /| | / ___// _ \ / __ \ / //_// __  /"
echo " / ___ |/ /__ /  __// / / // ,<  / /_/ / "
echo "/_/  |_|\___/ \___//_/ /_//_/|_| \__,_/ "
echo "========================================"
echo "Project by Kartik Sharma & Kshitij Tripathi"
echo ""
if test -f "nmap_scan.txt"; then
	echo "Converting NMAP scan to PDF..."
    python convert.py nmap_scan.txt 
fi
python convert.py nmap_scan.txt 
if test -f "wp_scan.txt"; then
	echo "Converting WordPress scan to PDF..."
    python convert.py wp_scan.txt 
fi
if test -f "joomla_scan.txt"; then
	echo "Converting Joomla scan to PDF..."
    python convert.py joom_scan.txt 
fi
if test -f "drupal_scan.txt"; then
	echo "Converting Drupal scan to PDF..."
    python convert.py drupe_scan.txt 
fi
echo "Merging All the PDFs together..."
#sleep 5 Not necessary
python PDFmerger.py
echo "Scan Report Completed..."
