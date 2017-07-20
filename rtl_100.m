indata=importdata('C:\Users\aoded\OneDrive\Documents\MATLAB\rtl_100.csv');
rtl_1M=indata.data(:,1)';
rtl_2M=indata.data(:,2)';

figure(7);
clf('reset');
hold on; box on;
set(gca, 'LineWidth', 2, 'FontSize',30);%, 'Position', [.1 .1 3 5]);%,'PlotBoxAspectRatio',[3 1.5 1]);%, 'FontWeight', 'bold');
title('RTL 100s - Sample Drop (k)')
xlabel('File Index')
ylabel('CDF');

plot(rtl_1M, 'r-s', 'LineWidth', 6, 'MarkerSize', 12)
plot(rtl_2M, 'b-^', 'LineWidth', 6, 'MarkerSize', 12)
%plot(perc_err, line_type{3}, 'LineWidth', 6, 'MarkerSize', 8)
ylim([0 1]);

xticks([1 2 3 4 5]);
xticklabels({'1', '2', '3', '4', '5'});
%xtickangle(20);

leg1=['RTL-1M'];% s=',num2str(scale)];
leg2=['RTL-2M'];% s=',num2str(scale)];
%leg3=['Percentage error']% s=',num2str(scale)];
legend(leg1,leg2,'Location','Best')
legend boxoff

filename = ['C:\Users\aoded\OneDrive\Documents\MATLAB\1.eps'];
saveas(gca,filename,'epsc');
hold off;