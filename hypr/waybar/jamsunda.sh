#!/bin/sh
case "$(date +%H)" in
    1|01 )
    ngaranjam="Tumorek"
    ;;
    2|02 )
    ngaranjam="Janari Leutik"
    ;;
    3|03 )
    ngaranjam="Janari Gedé"
    ;;
    4|04 )
    ngaranjam="Kongkorongok Hayam"
    ;;
    5|05 )
    ngaranjam="Balébat"
    ;;
    6|06 )
    ngaranjam="Carangcang Tihang"
    ;;
    7|07 )
    ngaranjam="Méléték Panonpoé"
    ;;
    8|08 )
    ngaranjam="Ngaluluh Taneuh"
    ;;
    9|09 )
    ngaranjam="Haneut Moyan"
    ;;
    10 )
    ngaranjam="Rumangsang"
    ;;
    11 )
    ngaranjam="Pecat Sawed"
    ;;
    12 )
    ngaranjam="Tangagé/Manceran"
    ;;
    13 )
    ngaranjam="Lingsir Ngulon"
    ;;
    14 )
    ngaranjam="Kalangkang Satungtung"
    ;;
    15 )
    ngaranjam="Méngok"
    ;;
    16 )
    ngaranjam="Tunggang Gunung"
    ;;
    17 )
    ngaranjam="Sariak Layung"
    ;;
    18 )
    ngaranjam="Sareupna/Sande Kala"
    ;;
    19 )
    ngaranjam="Harieum Beungeut"
    ;;
    20 )
    ngaranjam="Sareureuh Budak"
    ;;
    21 )
    ngaranjam="Tumoké"
    ;;
    22 )
    ngaranjam="Sareureuh Kolot"
    ;;
    23 )
    ngaranjam="Indung Peuting"
    ;;
    * )
    ngaranjam="Tengah Peuting Ngaweng-Ngaweng"
    ;;
esac
jam=$(date +"%H:%M")" - "
while getopts "ptf:" opt; do
    case "$opt" in
    h|\?)
        echo "Pemakaian: $0 [-t] [-p] [-f 12/24]"
        echo "t=tanggal, nampilkeun tanggal"
        echo "p=poe, nampilkeun nami poe ayeuna"
        echo "f=format, 12 jam atawa 24 jam (default: 24 jam)"
        exit 0
        ;;
    p)  p=1
        case "$(date +%A)" in
            Sunday | Minggu )
            poe="Minggu, "
            ;;
            Monday | Senin )
            poe="Senén, "
            ;;
            Tuesday | Selasa )
            poe="Salasa, "
            ;;
            Wednesday | Rabu )
            poe="Rebo, "
            ;;
            Thursday | Kamis )
            poe="Kemis, "
            ;;
            Friday | Jumat | Jum\'at )
            poe="Juma'ah, "
            ;;
            Saturday | Sabtu )
            poe="Saptu, "
            ;;
        esac
        ;;
    t)  t=1
        tanggal=$(date +"%d-%b-%Y")" | "
        ;;
    f)  f=$OPTARG
        case "$f" in
            12)
            jam=$(date +"%I:%M %p")" - "
            ;;
        esac
        ;;
    esac
done
echo "$tanggal$poe$jam$ngaranjam"
