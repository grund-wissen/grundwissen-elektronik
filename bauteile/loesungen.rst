.. _Lösungen zu elektronischen Bauteilen:

Lösungen zu elektronischen Bauteilen
====================================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben zu
elektronischen Bauteilen>` zum Abschnitt :ref:`Widerstände
<Widerstände>`.


.. rubric:: Lösungen zu Widerständen 

----

.. _Widerstand-01-Lösung:

* Der erste Ring ist braun, somit ist die erste Ziffer des Widerstandswertes
  gleich :math:`1`. Der zweite Ring ist schwarz, somit ist die zweite Ziffer
  des Widerstandswertes gleich :math:`0`. Der dritte Ring ist gelb, somit sind
  vier Nullen an den Zahlenwert anzuhängen. Insgesamt ergibt sich somit ein
  Widerstandswert von :math:`\unit[100\,000]{\Omega } = \unit[100]{k \Omega }`.

  .. figure::
      ../pics/bauteile/widerstand-farbringe-01-loesung.png
      :name: fig-widerstand-farbringe-01-loesung
      :alt:  fig-widerstand-farbringe-01-loesung
      :align: center
      :width: 30%

      Farbringe-Beispiel 01 (Lösung).

      .. only:: html
      
          :download:`SVG: Farbringe-Beispiel 01 (Lösung)
          <../pics/bauteile/widerstand-farbringe-01-loesung.svg>`

  Der goldfarbene Ring am rechten Rand zeigt an, dass der Toleranzbereich bei
  :math:`5\%` liegt. Der tatsächliche Wert des Widerstands liegt somit
  zwischen :math:`\unit[95]{k \Omega }` und :math:`\unit[105]{k \Omega }`.

  :ref:`Zurück zur Aufgabe <Widerstand-01>`

----

.. _Widerstand-02-Lösung:

* Die ersten beiden Ringe des Widerstands sind rot, somit haben die ersten
  beiden Ziffern des Widerstandswertes jeweils den Wert :math:`2`. Der dritte
  Ring ist orange, so dass an den Zahlenwert drei Nullen anzuhängen sind. Der
  Widerstand hat somit einen Wert von :math:`\unit[22\,000]{\Omega } =
  \unit[22]{k \Omega }`.

  .. figure::
      ../pics/bauteile/widerstand-farbringe-02-loesung.png
      :name: fig-widerstand-farbringe-02-loesung
      :alt:  fig-widerstand-farbringe-02-loesung
      :align: center
      :width: 30%

      Farbringe-Beispiel 02 (Lösung).

      .. only:: html
      
          :download:`SVG: Farbringe-Beispiel 02 (Lösung)
          <../pics/bauteile/widerstand-farbringe-02-loesung.svg>`

  :ref:`Zurück zur Aufgabe <Widerstand-02>`

----

.. _Widerstand-03-Lösung:

* Der Zahlenwert :math:`332` des Widerstands hat drei von Null verschiedene
  Zahlenziffern; somit muss es sich um einen Metallschicht-Widerstand mit
  fünf Ringen handeln. Die ersten beiden Ziffern des Zahlenwertes sind
  jeweils :math:`3`; somit müssen die ersten beiden Farbringe orange sein. 
  Die dritte Ziffer ist  :math:`2`; somit muss der dritte Farbring rot sein. 
  Es muss keine Null angehängt werden, somit ist der vierte Farbring schwarz. 

  .. figure::
      ../pics/bauteile/widerstand-farbringe-03-loesung.png
      :name: fig-widerstand-farbringe-03-loesung
      :alt:  fig-widerstand-farbringe-03-loesung
      :align: center
      :width: 30%

      Farbringe-Beispiel 03 (Lösung).

      .. only:: html
      
          :download:`SVG: Farbringe-Beispiel 03 (Lösung)
          <../pics/bauteile/widerstand-farbringe-03-loesung.svg>`


  Der fünfte Farbring ist ohne Angabe eines Toleranzbereiches nicht
  festgelegt. (Metallschicht-Widerstände haben üblicherweise einen
  Toleranzbereich von :math:`1\%` oder geringer.)

  :ref:`Zurück zur Aufgabe <Widerstand-03>`

----

.. _Widerstand-04-Lösung:

* Der Widerstand hat fünf Ringe, somit geben die ersten drei Ziffern den
  Zahlenwert und die vierte Ziffer den Multiplikator bzw. die Anzahl an Nullen
  an. 
  
  Der erste Ring ist braun, somit ist die erste Ziffer des Widerstandswertes
  gleich :math:`1`. Der zweite Ring ist grün, somit ist die zweite Ziffer des
  Widerstandswertes gleich :math:`5`. Der dritte Ring ist schwarz, somit ist
  die dritte Ziffer des Widerstandswertes gleich :math:`0`. Der vierte Ring
  ist orange, somit sind drei Nullen an den Zahlenwert anzuhängen. Insgesamt
  ergibt sich somit ein Widerstandswert von :math:`\unit[150\,000]{\Omega } =
  \unit[150]{k \Omega }`.

  .. figure::
      ../pics/bauteile/widerstand-farbringe-04-loesung.png
      :name: fig-widerstand-farbringe-04-loesung
      :alt:  fig-widerstand-farbringe-04-loesung
      :align: center
      :width: 30%

      Farbringe-Beispiel 04 (Lösung).

      .. only:: html
      
          :download:`SVG: Farbringe-Beispiel 04 (Lösung)
          <../pics/bauteile/widerstand-farbringe-04-loesung.svg>`

  Der fünfte Ring ist violett, somit liegt der Toleranzbereich bei
  :math:`0,1\%`. Der tatsächliche Wert des Widerstands liegt somit
  zwischen :math:`\unit[95]{k \Omega }` und :math:`\unit[105]{k \Omega }`.

  :ref:`Zurück zur Aufgabe <Widerstand-04>`

----

.. rubric:: Lösungen zu Transformatoren

----

.. _Transformator-01-Lösung:

* Um die Windungszahl der Sekundärspule zu bestimmen, löst man die 
  Transformator-Gleichung nach :math:`n _{\rm{2}}` auf:

  .. math::
      
      \frac{U _{\rm{1}} }{U _{\rm{2}} } = \frac{n _{\rm{1}} }{n _{\rm{2}} } \quad
      \Leftrightarrow \quad n _{\rm{2}} = \frac{n _{\rm{1}} \cdot U _{\rm{1}}
      }{U _{\rm{2}} } 
  
  Eingesetzt ergibt sich mit :math:`n _{\rm{1}} = 300`,  :math:`U _{\rm{1}} =
  \unit[230]{V}` und :math:`U2 = \unit[100]{V}`:

  .. math::
      
      n _{\rm{2}} = \frac{n _{\rm{1}} \cdot U _{\rm{1}}
      }{U _{\rm{2}} } =  \frac{300 \cdot \unit[230]{V}}{\unit[100]{V}} = 690

  Die Sekundärspule muss somit :math:`n _{\rm{2}} = 690` Windungen besitzen.

  :ref:`Zurück zur Aufgabe <Transformator-01>`

----

.. _Transformator-02-Lösung:

* Die Windungszahlen stehen nach der Transformator-Gleichung :math:`\frac{n
  _{\rm{1}} }{n _{\rm{2}} } = \frac{U _{\rm{1}} }{U _{\rm{2}} }` im gleichen
  Verhältnis wie die anliegenden Spannungen. An der Spule mit der höheren
  Anzahl an Windungen liegt daher auch stets die höhere Spannung, an der Spule
  mit der geringeren Anzahl an Windungen die niedrigere Spannung an.

  :ref:`Zurück zur Aufgabe <Transformator-02>`

----

.. _Transformator-03-Lösung:

* Um die Stromstärke in der Sekundärspule zu bestimmen, löst man die
  Transformator-Gleichung nach :math:`I _{\rm{2}}` auf:

  .. math::
      
      \frac{I _{\rm{1}} }{I _{\rm{2}} } = \frac{n _{\rm{2}} }{n _{\rm{1}} }
      \quad \Leftrightarrow \quad I _{\rm{2}} = \frac{n _{\rm{1}} \cdot I
      _{\rm{1}} }{n _{\rm{2}} } 

  Eingesetzt ergibt sich mit :math:`n _{\rm{1}} = 300`, :math:`n _{\rm{2}}  =
  1200` und :math:`I _{\rm{1}} = \unit[2]{A}`:

  .. math::
      
      I _{\rm{2}} = \frac{n _{\rm{1}} \cdot I _{\rm{1}} }{n _{\rm{2}} } =
      \frac{300 \cdot \unit[2]{A}}{1200} = \unit[0,5]{A}

  Die Stromstärke in der Sekundärspule des Transformators beträgt somit
  :math:`I _{\rm{2}} = \unit[0,5]{A}`.

  :ref:`Zurück zur Aufgabe <Transformator-03>`


.. raw:: latex

    \rule{\linewidth}{0.5pt}

.. raw:: html

    <hr/>
    
.. only:: html

    :ref:`Zurück zum Skript <Elektronische Bauteile>`


