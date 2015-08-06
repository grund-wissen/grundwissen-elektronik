.. index:: Transformator
.. _Transformator:
.. _Transformatoren:

Transformatoren
---------------

Transformatoren sind Bauteile, die eine Wechselspannung (oder pulsierende
Gleichspannung) in eine betragsmäßig höhere oder niedrigere Spannung umwandeln
können.

Hierzu ist ein Transformator stets aus zwei Spulen aufgebaut, die sich auf den
gegenüber liegenden Seiten eines Eisen- oder Ringkerns befinden. Die Spule, an
der die Eingangsspannung anliegt, wird als Primärspule, die andere als
Sekundärspule bezeichnet.

.. figure::
    ../pics/bauteile/schaltzeichen-transformator.png
    :name: fig-schaltzeichen-transformator
    :alt:  fig-schaltzeichen-transformator
    :align: center
    :width: 30%

    Schaltzeichen eines Transformators.

    .. only:: html

        :download:`SVG: Schaltzeichen Transformator
        <../pics/bauteile/schaltzeichen-transformator.svg>`

Das Verhältnis aus der Anzahl an Windungen :math:`n _{\rm{1}}` der Primärspule
zur Anzahl an Windungen :math:`n _{\rm{2}}` der Sekundärspule bestimmt das
Verhältnis von der Eingangsspannung :math:`U _{\rm{1}}`  zur Ausgangsspannung
:math:`U _{\rm{2}}`:

.. math::
    :label: eqn-transformator

    \frac{n _{\rm{1}}}{n _{\rm{2}}} = \frac{U _{\rm{1}}}{U _{\rm{2}}}


Die Stromstärken verhalten sich dabei genau umgekehrt wie die Spannungen:

.. math::
    :label: eqn-transformator-2

    \frac{I _{\rm{1}} }{ I _{\rm{2}}} = \frac{ U _{\rm{2}}}{U _{\rm{1}}}

Damit wird von einem (idealen) Transformator genauso viel elektrische Leistung
aufgenommen wie abgegeben: :math:`U _{\rm{1}} \cdot I _{\rm{1}} = U _{\rm{2}}
\cdot I _{\rm{2}}`. In der Praxis rechnet man zur Zahl der Windungen :math:`n
_{\rm{2}}` der Sekundärseite meist :math:`10\%`  hinzu, um die Energieverluste
durch das Aufwärmen des Transformators auszugleichen.

*Beispiel:*

* Um die Netzspannung von :math:`U _{\rm{1}} = \unit[230]{V}` auf beispielsweise
  :math:`U _{\rm{2}} = \unit[12]{V}` herunter zu regeln, benötigt man folgendes
  Verhältnis an Windungszahlen:

  .. math::

      \frac{n _{\rm{1}}}{n _{\rm{2}}} &= \frac{U _{\rm{1}}}{U _{\rm{2}}} =
      \frac{\unit[230]{V}}{\unit[12]{V}} \approx  19,2 \\[10pt]
      \Rightarrow n _{\rm{1}} &= 19,2 \cdot n _{\rm{2}}

  Auf der Primärseite müssen also rund :math:`19` mal mehr Windungen
  aufgebracht werden als auf der Sekundärseite.

Werden die Eingangs- und Ausgangsanschlüsse des Transformators umgetauscht,
so kann man (theoretisch) mit dem gleichen Transformator eine Wechselspannung
von :math:`U _{\rm{1}} = \unit[12]{V}` auf :math:`U _{\rm{2}} = \unit[230]{V}`
hochtransformieren.


