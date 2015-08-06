.. _Lösungen zu Reihen- und Parallelschaltungen:

Lösungen zu Reihen- und Parallelschaltungen
===========================================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben zu
Reihen- und Parallelschaltungen>` zum Abschnitt :ref:`Reihen- und
Parallelschaltungen <Reihen- und Parallelschaltungen>`.


.. rubric:: Lösungen zu Reihen- und Parallelschaltungen von Stromquellen

----

.. _Reihen-und-Parallelschaltung-Stromquellen-01-Lösung:

* Bei einer Reihenschaltung von :math:`n` Stromquellen addieren sich die Werte
  der Spannungen :math:`U _{\rm{1}},\,  U _{\rm{2}} ,\, \ldots ,\, U
  _{\rm{n}}` zu einer Gesamtspannung :math:`U _{\rm{ges}}`. Wenn drei
  Batterien mit einer Spannung von je :math:`\unit[1,5]{V}` in Reihe
  geschaltet werden, ergibt sich somit folgende Gesamt-Spannung:

  .. math::
      
      U _{\rm{ges}} &= U _{\rm{1}} + U _{\rm{2}} + U _{\rm{3}}
      = \unit[1,5]{V} + \unit[1,5]{V} + \unit[1,5]{V} = \unit[4,5]{V}

  Bei einer Parallelschaltung von (gleichartigen) Stromquellen ist die
  Gesamtspannung gleich der Spannung einer einzelnen Stromquelle. [#]_ Eine
  Parallelschaltung zweier :math:`\unit[1,5]{V}`-Batterien liefert somit eine
  Gesamt-Spannung von ebenfalls :math:`\unit[1,5]{V}`.

  :ref:`Zurück zur Aufgabe <Reihen-und-Parallelschaltung-Stromquellen-01>`

----

.. rubric:: Lösungen zu Reihen- und Parallelschaltungen von Widerständen

----

.. _Reihen-und-Parallelschaltung-Widerstände-01-Lösung:

* In einer Parallelschaltung ist die Gesamt-Stromstärke :math:`I _{\rm{ges}}`
  gleich der Summe der (Teil-)Stromstärken :math:`I _{\rm{1}} ,\, I _{\rm{2}}
  ,\, \ldots ,\, I _{\rm{n}}`. Betragen die Stromstärken :math:`I _{\rm{1}}`
  und :math:`I _{\rm{2}}` in zwei Stromzweigen :math:`\unit[1,8]{A}` bzw.
  :math:`\unit[2,2]{A}`, so ergibt sich damit folgende Gesamt-Stromstärke:

  .. math::
    
      I _{\rm{ges}} = I _{\rm{1}} + I _{\rm{2}} 
      = \unit[1,8]{A} + \unit[2,2]{A} = \unit[4,0]{A}
  
  Die Gesamt-Stromstärke beträgt somit :math:`I _{\rm{ges}} = \unit[4,0]{A}`. 

  :ref:`Zurück zur Aufgabe <Reihen-und-Parallelschaltung-Widerstände-01>`

----

.. _Reihen-und-Parallelschaltung-Widerstände-02-Lösung:

* Bei einer Reihenschaltung ist der Gesamtwiderstand :math:`R _{\rm{ges}}`
  gleich der Summe der einzelnen Widerstandswerte; für eine Reihenschaltung
  zweier Widerstände  :math:`R _{\rm{1}} = \unit[100]{\Omega }` und :math:`R
  _{\rm{2}} = \unit[50]{\Omega }` gilt somit:

  .. math::
      
      R _{\rm{ges}} = R _{\rm{1}} + R _{\rm{2}} = \unit[100]{\Omega } +
      \unit[50]{\Omega } = \unit[150]{\Omega }

  Durch Einsetzen des Werts der anliegenden Spannung :math:`U _{\rm{ges}} =
  \unit[9]{V}` und des Gesamtwiderstandes :math:`R _{\rm{Ges}} =
  \unit[150]{\Omega }` in das Ohmsche Gesetz :math:`U _{\rm{ges}} = R
  _{\rm{ges}} \cdot I` folgt damit für die fließende Stromstärke :math:`I`:
  
  .. math::
      
      U _{\rm{ges}} = R _{\rm{ges}} \cdot I \quad \Leftrightarrow \quad I =
      \frac{U _{\rm{ges}}}{R _{\rm{ges}}} 
  
  .. math::
      
      I = \frac{U _{\rm{ges}}}{R _{\rm{ges}}} =
      \frac{\unit[9]{V}}{\unit[150]{\Omega }} = \unit[0,06]{A} = \unit[60]{mA}
  
  Die Stromstärke beträgt somit :math:`I = \unit[60]{mA}` (an allen Stellen
  der Reihenschaltung). Wiederum mit Hilfe des Ohmschen Gesetzes können damit
  die beiden Teilspannungen :math:`U _{\rm{1}} = R _{\rm{1}} \cdot I` und
  :math:`U _{\rm{2}} = R _{\rm{2}} \cdot I` an den beiden Widerständen
  berechnet werden:

  .. math::
      
      U _{\rm{1}} &= R _{\rm{1}} \cdot I = \unit[100]{W} \cdot \unit[0,06]{A} =
      \unit[6]{V} \\[6pt]
      U _{\rm{2}} &= R _{\rm{1}} \cdot I = \unit[50]{W} \cdot \unit[0,06]{A} =
      \unit[3]{V} 
  
  Die beiden Teilspannungen :math:`U _{\rm{1}}` und :math:`U2` betragen somit
  :math:`\unit[6]{V}` bzw. :math:`\unit[3]{V}`. In der Summe ergeben sie die
  Gesamtspannung :math:`U _{\rm{ges}} = \unit[9]{V}`, zueinander stehen sie im
  gleichen Verhältnis wie die Werte :math:`R _{\rm{1}}` und :math:`R
  _{\rm{2}}` der Widerstände :math:`(\frac{U _{\rm{1}} }{U _{\rm{2}} } =
  \frac{R _{\rm{1}} }{R _{\rm{2}} } = \frac{2}{1})`.

  :ref:`Zurück zur Aufgabe <Reihen-und-Parallelschaltung-Widerstände-02>`

----

.. _Reihen-und-Parallelschaltung-Widerstände-03-Lösung:

* Bei einer Parallelschaltung ist der Kehrwert des Gesamtwiderstands
  :math:`\frac{1}{R _{\rm{ges}}}` gleich der Summe der Kehrwerte der einzelnen
  Widerstandswerte; für eine Reihenschaltung zweier Widerstände  :math:`R
  _{\rm{1}} = \unit[100]{\Omega }` und :math:`R _{\rm{2}} = \unit[50]{\Omega
  }` gilt somit:

  .. math::
      
      \frac{1}{R _{\rm{ges}}} = \frac{1}{R _{\rm{1}} } + \frac{1}{R _{\rm{2}}
      } = \frac{1}{\unit[100]{\Omega }} + \frac{1}{\unit[50]{\Omega }} =
      \unit[\frac{3}{100} ]{\frac{1}{\Omega }} 
      
  .. math::
      
      \Rightarrow R _{\rm{ges}} = \unit[\frac{100}{3}]{\Omega } \approx
      \unit[33,3]{\Omega }

  Durch Einsetzen des Werts der anliegenden Spannung :math:`U = \unit[9]{V}`
  und des Gesamtwiderstandes :math:`R _{\rm{Ges}} = \unit[33,3]{\Omega }` in
  das Ohmsche Gesetz :math:`U = R \cdot I` folgt damit für die im
  unverzweigten Teil fließende Stromstärke :math:`I _{\rm{ges}}`:
  
  .. math::
      
      U = R _{\rm{ges}} \cdot I _{\rm{ges}} \quad \Leftrightarrow \quad I =
      \frac{U}{R _{\rm{ges}}} 
  
  .. math::
      
      I _{\rm{ges}} = \frac{U}{R _{\rm{ges}}} =
      \frac{\unit[9]{V}}{\unit[33,3]{\Omega }} = \unit[0,27]{A} =
      \unit[270]{mA}
  
  Die Stromstärke beträgt im unverzweigten Teil der Schaltung somit :math:`I =
  \unit[270]{mA}`.

  :ref:`Zurück zur Aufgabe <Reihen-und-Parallelschaltung-Widerstände-03>`

----

.. _Reihen-und-Parallelschaltung-Widerstände-04-Lösung:

* Bei einer Parallelschaltung lässt sich der Kehrwert des Gesamtwiderstands
  :math:`\frac{1}{R _{\rm{ges}}}` als Summe der Kehrwerte der einzelnen
  Widerstandswerte berechnen:

  .. math::
      
      \frac{1}{R _{\rm{ges}}} = \frac{1}{R _{\rm{1}} } + \frac{1}{R _{\rm{2}}
      } + \frac{1}{R _{\rm{3}} } = \frac{1}{\unit[100]{\Omega }} +
      \frac{1}{\unit[470]{\Omega }} + \frac{1}{\unit[1\,000]{\Omega }} 
      \approx \unit[0,013]{\frac{1}{\Omega } } 

  .. math::
      
      \Rightarrow R _{\rm{ges}} \approx \unit[76,2]{\Omega }

  Die Spannung :math:`U= \unit[9]{V}` bleibt an allen Stellen der
  Parallelschaltung unverändert. Die Gesamt-Stromstärke :math:`I _{\rm{ges}}`
  sowie die Stromstärken :math:`I _{\rm{1}} ,\, I _{\rm{2}} ,\, I _{\rm{3}}`
  durch die Widerstände  :math:`R _{\rm{1}} ,\, R _{\rm{2}} ,\, R _{\rm{3}}`
  lassen sich mit Hilfe des Ohmschen Gesetzes berechnen:

  .. math::
      
      I _{\rm{ges}} = \frac{U}{R _{\rm{ges}}} &=
      \frac{\unit[9]{V}}{\unit[76,2]{\Omega }} =~ \unit[0,12]{A} \\[6pt]
      I _{\rm{1}} = \frac{U}{R _{\rm{1}}} &=
      \frac{\unit[9]{V}}{\unit[100]{\Omega }} =~ \unit[0,09]{A} \\[4pt]
      I _{\rm{2}} = \frac{U}{R _{\rm{2}}} &=
      \frac{\unit[9]{V}}{\unit[470]{\Omega }} =~ \unit[0,02]{A} \\[4pt]
      I _{\rm{3}} = \frac{U}{R _{\rm{3}}} &=
      \frac{\unit[9]{V}}{\unit[1\,000]{\Omega }} =~ \unit[0,01]{A} 
  
  Bei einer Reihenschaltung lässt sich der Gesamtwiderstand :math:`R
  _{\rm{ges}}` als Summe der einzelnen Widerstandswerte berechnen:

  .. math::
      
      R _{\rm{ges}} = R _{\rm{1}} + R _{\rm{2}} + R _{\rm{3}} =
      \unit[100]{\Omega } + \unit[470]{\Omega } + \unit[1\,000]{\Omega }
      = \unit[1\,570]{\Omega }
  
  Durch Einsetzen der anliegenden Spannung :math:`U _{\rm{ges}} = \unit[9]{V}`
  und des Gesamtwiderstands :math:`R _{\rm{ges}} = \unit[1\,570]{\Omega }` in
  das Ohmsche Gesetz folgt:

  .. math::
      
      U _{\rm{ges}} = R _{\rm{ges}} \cdot I \quad \Leftrightarrow \quad I =
      \frac{U _{\rm{ges}}}{R _{\rm{ges}} } 
  
  .. math::
      
      I _{\rm{ges}} = \frac{U}{R _{\rm{ges}}} =
      \frac{\unit[9]{V}}{\unit[1570]{\Omega }} \approx \unit[0,0057]{A} =
      \unit[5,7]{mA}

  Auch die an den einzelnen Widerständen anliegenden Spannungen lassen sich
  mit Hilfe des Ohmschen Gesetzes berechnen, wenn für die Stromstärke
  :math:`I = I _{\rm{ges}} \approx \unit[0,0057]{A}` eingesetzt wird:

  .. math::
      
      U _{\rm{1}} &= R _{\rm{1}} \cdot I \approx  \unit[100]{\Omega } \cdot
      \unit[0,0057]{A} \approx \unit[0,6]{V} \\[4pt]
      U _{\rm{2}} &= R _{\rm{2}} \cdot I \approx  \unit[470]{\Omega } \cdot
      \unit[0,0057]{A} = \unit[2,7]{V} \\[4pt]
      U _{\rm{3}} &= R _{\rm{3}} \cdot I \approx  \unit[1\,000]{\Omega } \cdot
      \unit[0,0057]{A} = \unit[5,7]{V}

  Die Summe der drei Teilspannungen entspricht (von Rundungsfehlern abgesehen)
  wieder der Gesamtspannung :math:`(U _{\rm{ges}} = U _{\rm{1}} + U _{\rm{2}}
  + U _{\rm{3}} = \unit[9]{V})`. 

  :ref:`Zurück zur Aufgabe <Reihen-und-Parallelschaltung-Widerstände-04>`

----

.. _Reihen-und-Parallelschaltung-Widerstände-05-Lösung:

* Die Parallelschaltung der beiden Widerstände :math:`R _{\rm{1}} =
  \unit[470]{\Omega }` und :math:`R _{\rm{2}} = \unit[220]{\Omega }` wirkt
  nach außen wie ein einzelner "Ersatzwiderstand" :math:`R _{\rm{Ers}}` mit
  folgendem Wert:

   .. math::
       
       \frac{1}{R _{\rm{Ers}}} = \frac{1}{R _{\rm{1}} } + \frac{1}{R2} =
       \unit[1]{\unit[470]{\Omega }} + \unit[1]{\unit[220]{\Omega }} \approx
       \unit[0,0067]{\frac{1}{\Omega } } 

  .. math::
      
      \Rightarrow R _{\rm{Ers}} \approx \unit[150]{\Omega }
  
  Der gesamte Stromkreis kann damit als eine Reihenschaltung des
  Ersatzwiderstands :math:`R _{\rm{Ers}} \approx \unit[150]{\Omega }` 
  und des Widerstands :math:`R _{\rm{3}} = \unit[560]{\Omega }` aufgefasst
  werden. Für den Gesamtwiderstand :math:`R _{\rm{ges}}` folgt:
   
  .. math::
      
      R _{\rm{ges}} = R _{\rm{Ers}} + R _{\rm{3}} \approx \unit[150]{\Omega } +
      \unit[560]{\Omega } = \unit[710]{\Omega }
  
  Mit dem Ohmschen Gesetz lässt sich in Folge die Stromstärke :math:`I
  _{\rm{ges}}` im unverzweigten Teil des Stromkreises :math:`(U _{\rm{ges}} =
  \unit[9]{V},\, R _{\rm{ges}} \approx \unit[710]{\Omega })` bestimmen:

  .. math::
      
      U = R _{\rm{ges}} \cdot I _{\rm{ges}} \quad \Leftrightarrow \quad I =
      \frac{U}{R _{\rm{ges}}} 
  
  .. math::
      
      I _{\rm{ges}} = \frac{U _{\rm{ges}}}{R _{\rm{ges}}} \approx
      \frac{\unit[9]{V}}{\unit[710]{\Omega }} \approx \unit[0,013]{A} =
      \unit[13]{mA}

  Mit :math:`I = I _{\rm{ges}} \approx \unit[0,013]{A}` lassen sich die an den
  Widerständen :math:`R _{\rm{Ers}}` und :math:`R _{\rm{3}}` anliegenden
  Spannungen :math:`U _{\rm{Ers}}` bzw. :math:`U _{\rm{3}}` bestimmen:

  .. math::
      
      U _{\rm{Ers}} &= R _{\rm{Ers}} \cdot I \approx \unit[150]{\Omega} \cdot
      \unit[0,013]{A}  \approx  \unit[1,9]{V} \\[6pt]
      U _{\rm{3}} &= R _{\rm{3}} \cdot I \approx \unit[560]{\Omega } \cdot
      \unit[0,013]{A} \approx \unit[7,1]{V}

  Die Spannung :math:`U _{\rm{Ers}} \approx \unit[1,9]{V}` liegt an beiden
  parallelen Widerständen :math:`R _{\rm{1}}` und :math:`R _{\rm{2}}` an. Für
  die Stromstärken :math:`I _{\rm{1}}` und :math:`I _{\rm{2}}` in diesen
  beiden Stromzweigen ergibt sich somit:

  .. math::
      
      I _{\rm{1}} = \frac{U _{\rm{Ers}}}{R _{\rm{1}}} \approx
      \frac{\unit[1,9]{V}}{\unit[470]{\Omega}} \approx \unit[0,004]{A} \\[6pt]
      I _{\rm{1}} = \frac{U _{\rm{Ers}}}{R _{\rm{2}}} \approx
      \frac{\unit[1,9]{V}}{\unit[220]{\Omega}} \approx \unit[0,009]{A}

  Die Summe der beiden Stromstärken ist wiederum gleich der Stromstärke
  :math:`I _{\rm{ges}}` im unverzweigten Stromkreis. 

  :ref:`Zurück zur Aufgabe <Reihen-und-Parallelschaltung-Widerstände-04>`
    
.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#]  Durch eine Parallelschaltung mehrerer Batterien oder Akkus kann
        allerdings deren gespeicherte Energiemenge und damit die "Haltbarkeit"
        der Stromquelle vergrößert werden. 

.. raw:: latex

    \rule{\linewidth}{0.5pt}

.. raw:: html

    <hr/>
    
.. only:: html

    :ref:`Zurück zum Skript <Reihen- und Parallelschaltungen>`


