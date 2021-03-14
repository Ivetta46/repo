% Импортируйте данные из csv-файлов

% Определите константы
lambdaPr = 656.28; %нм
speedOfLight = 299792.458; %км/c

% Определите диапазон длин волн

% Рассчитайте скорости звезд относительно Земли

% Постройте график

% Сохраните график
spectra = importdata('spectra.csv');
lambdaStart = importdata('lambda_start.csv');
lambdaDelta = importdata('lambda_delta.csv');
starNames = importdata('star_names.csv');


nObs = size(spectra, 1);
lambdaEnd = lambdaStart + (nObs - 1) * lambdaDelta;
lambda = (lambdaStart : lambdaDelta : lambdaEnd)';
counStars = size(spectra, 2);

speed = linspace(0,0,counStars);
sHa = linspace(0,0,counStars);
idx = linspace(0,0,counStars);
lambdaHa = linspace(0,0,counStars);
z = linspace(0,0,counStars);

for i = 1:1:counStars
    s = spectra(:, i)
    [sHa(i), idx(i)] = min(s)
    lambdaHa(i) = lambda(idx(i));
    z(i) = (lambdaHa(i) / lambdaPr) - 1;
    speed(i) = z(i) * speedOfLight;
end
speed = speed'
fg1 = figure
set(gcf, 'visible', 'on')
xlabel('Длина волны, нм')
ylabel(['Интенсивность, эрг/см^2/с/', char(197)])
title('Спектры звезд')
hold on

for j = 1 : 1 : counStars
    if z(j) < 0
        plot(lambda, spectra(:, j), "--", 'LineWidth', 1)
    else
        plot(lambda, spectra(:, j), 'LineWidth', 3)
    end
end

legend(starNames)
grid on
text(lambdaStart + 5, max(max(spectra))* 1.05,'Соловьева Иветта, Б04-007')
hold off
movaway = starNames(speed' > 0);
saveas(fg1, 'spectraplot.png')
